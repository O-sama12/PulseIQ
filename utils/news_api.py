import os
import requests
import streamlit as st

# Load environment variables
load_dotenv()

API_KEY = st.secrets["NEWS_API_KEY"]

def get_news(category="technology"):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category={category}&"
        f"language=en&"
        f"pageSize=10&"
        f"apiKey={API_KEY}"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("articles", [])

    except requests.exceptions.RequestException as e:
        print("ERROR:", e)
        return []