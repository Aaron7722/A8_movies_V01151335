import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="🎬 Malayalam Movie Finder", page_icon="🎥", layout="centered")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Movies_database.csv")
    return df

movies = load_data()

st.title("🎬 Malayalam Movie Finder")
st.markdown("Select a genre to see all Malayalam movies in that category, along with details! 🍿")

# Define the fixed list of your famous genres
allowed_genres = ['Drama', 'Comedy', 'Romance', 'Thriller', 'Action', 'Crime', 'Mystery']

# Filter genres that actually exist in data
available_genres = sorted([genre for genre in allowed_genres if genre in movies['Genre'].unique()])

# Genre dropdown
selected_genre = st.selectbox("Choose a genre:", available_genres)

# Filter movies by genre
filtered = movies[movies['Genre'] == selected_genre]

if not filtered.empty:
    st.subheader(f"Movies in genre: {selected_genre}")
    for index, movie in filtered.iterrows():
        st.markdown(f"### 🎥 {movie['Title']} ({movie['Year']})")
        st.write(f"⭐ **IMDb Rating:** {movie['IMDb Rating']}")
        st.write(f"📝 **Description:** {movie['Short Description']}")
        st.markdown("---")
else:
    st.warning("No movies found in this genre!")

st.markdown("✅ *Built with Streamlit*")
