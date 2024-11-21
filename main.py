from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,Session
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import requests
from dotenv import load_dotenv
import os
import uuid

app = Flask(__name__)
load_dotenv()

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm password', validators=[DataRequired()])
    submit = SubmitField("Login")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        confirm_pass = form.confirm_password.data

        existing_user = mongo.db.user_posts.find_one({'username': user})
        if existing_user:
            message = "User is already registered"
            return render_template("register.html", form=form, message=message)
        
        if password != confirm_pass:
            message = "Passwords do not match"
            return render_template("register.html", form=form, message=message)
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = {
            'user': user,
            'hash_password': hashed_password
        }
        mongo.db.user_posts.insert_one(new_user)
        return redirect(url_for('login'))
    
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    message = None 
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        print(password)
        existing_user = mongo.db.user_posts.find_one({'user': user})

        if existing_user and bcrypt.check_password_hash(existing_user['hash_password'], password):
            message = "Login successful"
            return render_template("login.html", form=form, message=message)
        else:
            message = "Invalid username or password"
            return render_template("login.html", form=form, message=message)

    return render_template("login.html", form=form, message=message)

@app.route('/')
def home():
    return '<h1>Welcome Home</h1>'


@app.route('/google_login', methods=['POST'])
def google_login():
    token = request.json.get('id_token')
    response = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={token}')

    if response.status_code == 200:
        user_info = response.json()
        email = user_info.get('email')
        name = user_info.get('name')

        # Зберігаємо дані користувача у сесії (або базі даних)
        session['user'] = {'email': email, 'name': name}

        return jsonify({'status': 'success', 'email': email, 'name': name}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid token'}), 400

@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return render_template("dashboard.html", user=user)

# @app.route('/test_db')
# def test_db():
#     try:
#         users_count = mongo.db.user_posts
#         return f'Connected! Number of users: {users_count}'
#     except Exception as e:
#         return f"Database connection error: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="localhost",port=5003)
