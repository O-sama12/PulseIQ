# 🚀 PulseIQ

**AI-Powered Finance & Tech Insight Intelligence Platform**

PulseIQ is a Streamlit-based web application that curates real-time finance, technology, startup, and business insights into clean, digestible cards with AI-powered fake news detection.

# ✨ Features
- 📰 Real-time news from NewsAPI
- 📊 Category-based filtering (Finance, Tech, Startups, Business)
- 🔍 Smart search across headlines & descriptions
- 🔖 Bookmark system (session-based)
- 🧠 AI Fake News detection (Groq API)
- 🌙 Dark mode UI toggle
- 📤 Shareable insight cards
- ⚡ Clean modern dashboard UI

# 🧠 AI Feature
PulseIQ uses a lightweight AI agent to analyze article credibility and flag potential misinformation based on:
- Title & content patterns
- Sensational language detection
- AI-generated credibility score

# 🛠️ Tech Stack
- Python 🐍
- Streamlit ⚡
- NewsAPI 📰
- Groq AI API 🤖
- dotenv (local dev only)

# 📦 Installation
```bash
git clone https://github.com/O-sama12/pulseiq.git
cd pulseiq
pip install -r requirements.txt
```

# 🔐 Environment Variables
```toml
NEWS_API_KEY="your_newsapi_key"
groq_API_KEY="your_groq_api_key"
```

# ▶️ Run Locally
```bash
streamlit run app.py
```

# 🌐 Deployment
Deployed using Streamlit Community Cloud.

# 📌 Project Goal
To simplify how users consume financial and tech news by combining:
- AI summarization
- credibility detection
- and fast card-based UI

# 🏁 Status
✔ MVP Completed
✔ AI Integration Done
✔ Deployment Ready

# ⚡ Built With Focus
Built in a 24-hour hackathon sprint to demonstrate rapid AI product development.
