import streamlit as st
from utils.news_api import get_news

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PulseIQ",
    page_icon="📈",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stApp {
    background-color: #0E1117;
}

h1, h2, h3, p, div {
    color: white;
}

.insight-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #161B22;
    margin-bottom: 20px;
    border: 1px solid #30363D;
}

.category-tag {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 10px;
    background-color: #238636;
    color: white;
    font-size: 12px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 PulseIQ")

category = st.sidebar.radio(
    "Choose Category",
    ["Trending", "Finance", "Technology", "Startups", "Business"]
)

# ---------------- CATEGORY MAP ----------------
api_category_map = {
    "Trending": "technology",
    "Finance": "business",
    "Technology": "technology",
    "Startups": "technology",
    "Business": "business"
}

selected_api_category = api_category_map.get(
    category,
    "technology"
)

# ---------------- FETCH ARTICLES ----------------
articles = get_news(selected_api_category)

# ---------------- HEADER ----------------
st.title("🚀 PulseIQ")
st.caption("Real-Time Finance & Tech Insights")

# ---------------- TRENDING SECTION ----------------
if category == "Trending":
    st.subheader("🔥 Trending Insights")

# ---------------- EMPTY CHECK ----------------
if not articles:
    st.error("No articles found.")
    st.stop()

# ---------------- RENDER ARTICLES ----------------
for article in articles:

    title = article.get("title", "No Title")
    description = article.get(
        "description",
        "No Description Available"
    )

    source_url = article.get("url", "#")

    image_url = article.get("urlToImage")

    # ---------------- CARD ----------------
    with st.container():

        st.markdown(
            '<div class="insight-card">',
            unsafe_allow_html=True
        )

        # IMAGE
        if image_url:
            st.image(
                image_url,
                use_container_width=True
            )

        # TITLE
        st.markdown(f"## {title}")

        # DESCRIPTION
        st.write(description)

        # CATEGORY TAG
        st.markdown(
            f'<div class="category-tag">{category}</div>',
            unsafe_allow_html=True
        )

        st.write("")

        # BUTTONS
        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "🌐 Read Source",
                source_url,
                use_container_width=True
            )

        with col2:
            st.button(
                "🔖 Bookmark",
                key=title,
                use_container_width=True
            )

        st.markdown("</div>", unsafe_allow_html=True)