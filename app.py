import streamlit as st
from utils.news_api import get_news
from utils.fake_news_agent import analyze_fake_news

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PulseIQ",
    page_icon="⚡",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# ---------------- THEME TOGGLE ----------------
st.sidebar.title("⚙️ Settings")

dark_toggle = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)

st.session_state.dark_mode = dark_toggle

# ---------------- THEME COLORS ----------------
if st.session_state.dark_mode:

    BG = "#0B0F19"
    CARD = "rgba(22, 27, 34, 0.75)"
    TEXT = "white"
    BORDER = "rgba(255,255,255,0.1)"
    TAG = "#00C896"

else:

    BG = "#F3F6FC"
    CARD = "rgba(255,255,255,0.75)"
    TEXT = "#111111"
    BORDER = "rgba(0,0,0,0.08)"
    TAG = "#2563EB"

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(circle at top left, #1E293B 0%, {BG} 40%);
    color: {TEXT};
}}

h1, h2, h3, h4, h5, h6, p, div, span {{
    color: {TEXT};
}}

.insight-card {{
    padding: 24px;
    border-radius: 24px;
    background: {CARD};
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid {BORDER};
    margin-bottom: 28px;
    transition: 0.3s ease;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}}

.insight-card:hover {{
    transform: translateY(-5px) scale(1.01);
    box-shadow: 0 15px 40px rgba(0,0,0,0.35);
}}

.category-tag {{
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: {TAG};
    color: white;
    font-size: 12px;
    font-weight: 600;
    margin-top: 10px;
}}

.hero-title {{
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #00F5A0,
        #00D9F5,
        #7C4DFF
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.subtitle {{
    font-size: 1.1rem;
    opacity: 0.85;
    margin-bottom: 20px;
}}

section[data-testid="stSidebar"] {{
    background: rgba(15,23,42,0.75);
    backdrop-filter: blur(15px);
}}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 PulseIQ")

category = st.sidebar.radio(
    "Choose Category",
    [
        "Trending",
        "Finance",
        "Technology",
        "Startups",
        "Business"
    ]
)

# ---------------- BOOKMARKS ----------------
st.sidebar.markdown("---")
st.sidebar.subheader("🔖 Saved Bookmarks")

if st.session_state.bookmarks:

    for i, bookmark in enumerate(
        st.session_state.bookmarks
    ):

        col1, col2 = st.sidebar.columns([4, 1])

        with col1:

            st.markdown(
                f"[{bookmark['title']}]({bookmark['url']})"
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
with st.spinner(
    "⚡ Fetching real-time insights..."
):

    articles = get_news(
        selected_api_category
    )

# ---------------- HEADER ----------------
st.markdown(
    '<div class="hero-title">PulseIQ ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Finance & Tech Insight Intelligence</div>',
    unsafe_allow_html=True
)

# ---------------- SEARCH BAR ----------------
search_query = st.text_input(
    "🔍 Search Insights",
    placeholder="Search finance, AI, startups, crypto..."
)

# ---------------- TRENDING ----------------
if category == "Trending":

    st.subheader("🔥 Trending Insights")

    articles = articles[:5]

# ---------------- SEARCH FILTER ----------------
if search_query:

    filtered_articles = []

    for article in articles:

        title = article.get(
            "title",
            ""
        )

        description = article.get(
            "description",
            ""
        )

        combined_text = (
            title + " " + description
        ).lower()

        if search_query.lower() in combined_text:

            filtered_articles.append(
                article
            )

    articles = filtered_articles

# ---------------- EMPTY CHECK ----------------
if not articles:

    st.error(
        "No matching articles found."
    )

    st.stop()

# ---------------- DASHBOARD ----------------
col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📰 Articles",
        len(articles)
    )

with col2:

    st.metric(
        "🔖 Bookmarks",
        len(st.session_state.bookmarks)
    )

with col3:

    st.metric(
        "🔥 Category",
        category
    )

st.write("")

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

        # TAG
        st.markdown(
            f'<div class="category-tag">{category}</div>',
            unsafe_allow_html=True
        )

        st.write("")

        # BUTTONS
        col1, col2, col3, col4 = st.columns(4)

        # READ SOURCE
        with col1:

            st.link_button(
                "🌐 Source",
                source_url,
                use_container_width=True
            )

        # BOOKMARK
        with col2:

            if st.button(
                "🔖 Save",
                key=title,
                use_container_width=True
            ):

                already_exists = any(
                    bookmark["title"] == title
                    for bookmark
                    in st.session_state.bookmarks
                )

                if not already_exists:

                    st.session_state.bookmarks.append({
                        "title": title,
                        "url": source_url
                    })

                    st.toast(
                        "🔖 Bookmark Saved!"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Already bookmarked."
                    )

        # SHARE
        with col3:

            st.link_button(
                "📤 Share",
                source_url,
                use_container_width=True
            )

        # AI ANALYSIS
        with col4:

            if st.button(
                "🧠 AI Check",
                key=f"ai_{title}",
                use_container_width=True
            ):

                with st.spinner(
                    "AI analyzing credibility..."
                ):

                    st.toast(
                        "🧠 AI Agent Activated"
                    )

                    result = analyze_fake_news(
                        title,
                        description
                    )

                    result_lower = result.lower()

                    if (
                        "high" in result_lower
                        or "fake" in result_lower
                        or "misleading" in result_lower
                        or "sensational"
                        in result_lower
                    ):

                        st.markdown("""
                            <div style="
                            padding:16px;
                            border-radius:18px;
                            background:rgba(255,0,0,0.12);
                            border:1px solid rgba(255,0,0,0.35);
                            font-weight:700;
                            margin-top:12px;
                            margin-bottom:12px;
                            backdrop-filter: blur(12px);
                        ">
                        ⚠️ AI Warning: Potential Misinformation Detected
                        </div>
                        """, unsafe_allow_html=True)

                    else:

                        st.markdown("""
                        <div style="
                        padding:16px;
                        border-radius:18px;
                        background:rgba(0,255,150,0.12);
                        border:1px solid rgba(0,255,150,0.30);
                        font-weight:700;
                        margin-top:12px;
                        margin-bottom:12px;
                        backdrop-filter: blur(12px);
                    ">
                    ✅ AI Verdict: Appears Relatively Credible
                    </div>
                    """, unsafe_allow_html=True)

                    st.info(result)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )