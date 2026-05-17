import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_fake_news(title, description):

    prompt = f"""
    Analyze this news article.

    TITLE:
    {title}

    DESCRIPTION:
    {description}

    Detect:
    - fake news probability
    - sensationalism
    - clickbait signals
    - credibility issues

    Return in this format:

    Fake News Probability: X%
    Credibility Score: X/10
    Analysis: ...
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content