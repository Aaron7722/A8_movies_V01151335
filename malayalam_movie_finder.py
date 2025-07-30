import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="🎬 Malayalam Movie Finder", page_icon="🎥", layout="centered")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Movies_database.csv", encoding='utf-8', engine='python')

movies = load_data()

# Define your fixed list of genres
allowed_genres = ['Drama', 'Comedy', 'Romance', 'Thriller', 'Action', 'Crime', 'Mystery']
available_genres = sorted([genre for genre in allowed_genres if genre in movies['Genre'].unique()])

# Sidebar: genre filter
st.sidebar.header("🍿 Filter")
selected_genre = st.sidebar.selectbox("Choose a genre:", available_genres)

# Main area: show banner image at the top
st.image("banner.jpg", use_column_width=True)

# Quirky intro text
st.markdown("""
🍿🎥 **Movies are a great deal in our day-to-day lives — *especially* for Keralites! 🇮🇳❤️**

😅 But let’s be honest: it’s often super hard to get good suggestions for hidden gems or evergreen classics.

✨ So here’s a **fun little app** that suggests Malayalam movies based on your favorite genre! 🎞️👇

✅ **Pick a genre → get a list of movies with ratings & descriptions.**

Do enjoy... and see you at the movies! 🎬🤩🌟
""")

# Filter movies
filtered = movies[movies['Genre'] == selected_genre]

# Show movies
if not filtered.empty:
    st.subheader(f"Movies in genre: {selected_genre}")
    for _, movie in filtered.iterrows():
        st.markdown(f"### 🎥 {movie['Title']} ({movie['Year']})")
        st.write(f"⭐ **IMDb Rating:** {movie['IMDb Rating']}")
        st.write(f"📝 **Description:** {movie['Short Description']}")
        st.markdown("---")
else:
    st.warning("No movies found in this genre!")

st.markdown("✅ *Built with Streamlit*")
