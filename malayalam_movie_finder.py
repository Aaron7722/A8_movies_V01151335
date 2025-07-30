import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="🎬 Malayalam Movie Finder", page_icon="🎥", layout="centered")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Movies_database.csv", encoding='utf-8', engine='python')

movies = load_data()

# Define fixed list of genres
allowed_genres = ['Drama', 'Comedy', 'Romance', 'Thriller', 'Action', 'Crime', 'Mystery']
available_genres = sorted([genre for genre in allowed_genres if genre in movies['Genre'].unique()])

# App title
st.title("🎬 Malayalam Movie Finder")

# Sidebar
st.sidebar.header("Filter")
selected_genre = st.sidebar.selectbox("Choose a genre:", available_genres)

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

