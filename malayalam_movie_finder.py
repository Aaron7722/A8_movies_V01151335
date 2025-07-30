import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="🎬 Malayalam Movie Finder", page_icon="🎥", layout="centered")

# Load data
@st.cache_data
def load_data():
    # Use correct encoding to avoid UnicodeDecodeError
    return pd.read_csv("Movies_database.csv", encoding='utf-8', engine='python')

movies = load_data()

# Define your fixed list of genres
allowed_genres = ['Drama', 'Comedy', 'Romance', 'Thriller', 'Action', 'Crime', 'Mystery']

# Filter genres that actually exist in your data
available_genres = sorted([genre for genre in allowed_genres if genre in movies['Genre'].unique()])

# App title
st.title("🎬 Malayalam Movie Finder")

# Show dropdown in main area (not sidebar)
selected_genre = st.selectbox("Choose a genre:", available_genres)

# Filter movies by selected genre
filtered = movies[movies['Genre'] == selected_genre]

# Display movies
if not filtered.empty:
    for _, movie in filtered.iterrows():
        st.markdown(f"### 🎥 {movie['Title']} ({movie['Year']})")
        st.write(f"⭐ **IMDb Rating:** {movie['IMDb Rating']}")
        st.write(f"📝 **Description:** {movie['Short Description']}")
        st.markdown("---")
else:
    st.warning("No movies found in this genre!")

