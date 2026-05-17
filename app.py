import streamlit as st
from utils.news_api import get_news

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PulseIQ",
    page_icon="📈",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

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
    margin-bottom: 25px;
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

# ---------------- BOOKMARKS SIDEBAR ----------------
st.sidebar.markdown("---")
st.sidebar.subheader("🔖 Saved Bookmarks")

if st.session_state.bookmarks:

    for i, bookmark in enumerate(st.session_state.bookmarks):

        col1, col2 = st.sidebar.columns([4, 1])

        with col1:
            st.markdown(
                f"- [{bookmark['title']}]({bookmark['url']})"
            )
        with col2:
            if st.button(
                "❌",
                key=f"remove_{i}"
            ):
                st.session_state.bookmarks.pop(i)
                st.rerun()
else:
    st.sidebar.caption("No bookmarks yet.")

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
with st.spinner("Fetching latest insights..."):

    articles = get_news(selected_api_category)

# ---------------- HEADER ----------------
st.title("🚀 PulseIQ")
st.caption("Real-Time Finance & Tech Insights")

# ---------------- TRENDING SECTION ----------------
if category == "Trending":

    st.subheader("🔥 Trending Insights")

    articles = articles[:5]

# ---------------- EMPTY CHECK ----------------
if not articles:

    st.error("Unable to fetch articles.")

    st.stop()

# ---------------- RENDER ARTICLES ----------------
for article in articles:

    title = article.get(
        "title",
        "No Title"
    )

    description = article.get(
        "description",
        "No Description Available"
    )

    source_url = article.get(
        "url",
        "#"
    )

    image_url = article.get(
        "urlToImage"
    )

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
        col1, col2, col3 = st.columns(3)

        # READ SOURCE
        with col1:

            st.link_button(
                "🌐 Read Source",
                source_url,
                use_container_width=True
            )

        # BOOKMARK
        with col2:

            if st.button(
                "🔖 Bookmark",
                key=title,
                use_container_width=True
            ):

                already_exists = any(
                    bookmark["title"] == title
                    for bookmark in st.session_state.bookmarks
                )

                if not already_exists:

                    st.session_state.bookmarks.append({
                        "title": title,
                        "url": source_url
                    })

                    st.success("Added to bookmarks!")
                    st.rerun()

                else:
                    st.warning("Already bookmarked.")

        # SHARE
        with col3:

            st.link_button(
                "📤 Share",
                source_url,
                use_container_width=True
            )

        st.markdown("</div>", unsafe_allow_html=True)