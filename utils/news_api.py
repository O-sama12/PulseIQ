from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("NEWS_API_KEY not found in .env")


def get_news(category="technology"):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category={category}&"
        f"language=en&"
        f"pageSize=10&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    data = response.json()

    return data.get("articles", [])