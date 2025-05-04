
import requests
from bs4 import BeautifulSoup

def fetch_data_from_url_latvia():
    data = {}

    url = "https://www.lb.lt/en/authorisation-of-electronic-money-institutions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    divs = soup.select("div.media-body")

    for i, div in enumerate(divs[:9], start=1):
        title = div.find("h3")
        text = div.find("div", recursive=False)

        data[f"element_{i}_title"] = title.text.strip() if title else "No title"
        data[f"element_{i}_text"] = text.text.strip() if text else "No text"

    return data
