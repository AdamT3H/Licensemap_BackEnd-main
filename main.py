from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,Session
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import requests
from dotenv import load_dotenv
import os
from functools import wraps
import uuid
from flask_cors import CORS
from webSkreping import fetch_data_from_url_latvia
import jwt
import datetime
from flask import make_response
import secrets
from flask import g

app = Flask(__name__)
load_dotenv()
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])


app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
SECRET_KEY = "XGmot4oBwiNlScwOgwhI6h-rDU2O2YkSFXB5AhtplPM"

@app.route("/register", methods=["GET", "POST"])
def register():
    data = request.get_json()
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    confirm_password = data.get("confirmPassword")

    if not all([first_name, last_name, email, username, password, confirm_password]):
        return jsonify({"message": "All fields are required"}), 400

    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"}), 400

    existing_user = mongo.db.user_posts.find_one({'username': username})
    if existing_user:
        return jsonify({"message": "User is already registered"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'hash_password': hashed_password
    }

    insert_result = mongo.db.user_posts.insert_one(new_user)

    token = jwt.encode(
        {
            "user_id": str(insert_result.inserted_id),
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    response = make_response(jsonify({"message": "Registration successful"}))
    response.set_cookie(
        "token",
        token,
        httponly=True,
        samesite='Strict',
        secure=False,
        max_age=3600
    )

    return response, 201

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("token")
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user = data  # зберігаємо у flask.g
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/profile", methods=["GET"])
@token_required
def profile():
    return jsonify({"message": "User profile", "user": g.user}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    existing_user = mongo.db.user_posts.find_one({'username': username})

    if existing_user and bcrypt.check_password_hash(existing_user['hash_password'], password):
        token = jwt.encode(
            {
                "user_id": str(existing_user['_id']),
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        response = make_response(jsonify({"message": "Login successful"}))
        response.set_cookie(
            "token",
            token,
            httponly=True,
            samesite='Strict',
            secure=False, 
            max_age=3600
        )
        return response

    return jsonify({"message": "Invalid username or password"}), 401

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

if __name__ == "__main__":
    app.run(debug=True, host="localhost",port=5003)