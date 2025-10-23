import pickle
import streamlit as st
import requests
import pandas as pd

import requests
from requests.exceptions import RequestException

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    
#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         data = response.json()
        
#         if 'poster_path' in data and data['poster_path']:
#             return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
#         else:
#             return "https://via.placeholder.com/500x750.png?text=No+Image+Available"

#     except RequestException as e:
#         print("Network/API error:", e)
#         return "https://via.placeholder.com/500x750.png?text=No+Image+Available"

import requests
import time

def fetch_poster(movie_id, retries=3, delay=1):
    """Fetch movie poster from TMDb with retries and fallback image."""
    base_url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    fallback_image = "https://via.placeholder.com/500x750.png?text=No+Image+Available"

    for attempt in range(retries):
        try:
            response = requests.get(base_url.format(movie_id), timeout=5)
            
            # Handle bad or empty responses
            if response.status_code != 200:
                time.sleep(delay)
                continue

            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return fallback_image

        except requests.exceptions.RequestException:
            # Retry on network error
            time.sleep(delay)
    
    # Return fallback if all retries fail
    return fallback_image


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommender System')

moviesdict = pickle.load(open(r'C:\Users\mayan\Desktop\Portfolio Projects\Recommender_Systems\Zee_Movies_Recommender/movie_dict.pkl','rb'))
movies = pd.DataFrame(moviesdict)

# similarity = pickle.load(open(r'C:\Users\mayan\Desktop\Portfolio Projects\Recommender_Systems\Zee_Movies_Recommender/similarity.pkl','rb'))
import gzip, pickle
with gzip.open("similarity_compressed.pkl.gz", "rb") as f:
    similarity = pickle.load(f)


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



print(recommend('Gandhi'))