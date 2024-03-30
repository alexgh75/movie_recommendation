# Import python libraries
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import requests
from functions import cleanOperation, cleankSymbol, cleanDuration, preprocess

import streamlit as st
import pandas as pd
import requests

def ml():
    st.image('images/cinemas_a.jpg',width=500)
    st.title("Based on your preferences, we recommend you watch")

    # Load cinemas.csv
    cinemas = pd.read_csv("cinemas.csv")

    # Function to fetch movie details from TMDb
    def get_movie_details(movie_title, api_key):
        # Base URL for TMDb API
        base_url = "https://api.themoviedb.org/3/search/movie"

        # Parameters for the request
        params = {
            "api_key": api_key,
            "query": movie_title
        }

        # Send GET request to TMDb API
        response = requests.get(base_url, params=params)

        # Check if request was successful
        if response.status_code == 200:
            # Parse the response JSON
            results = response.json()["results"]

            # Check if there are any results
            if results:
                # Get the first result (most relevant)
                movie_details = results[0]
                return movie_details
            else:
                return None
        else:
            print("Error fetching movie details:", response.status_code)
            return None

    # Function to recommend a movie and redirect to its TMDb details
    def recommend_movie(new_movie, cinemas, api_key):
        new_movie = new_movie.lower()  # Convert input movie title to lowercase

        # Convert titles in cinemas DataFrame to lowercase for case-insensitive comparison
        cinemas['title'] = cinemas['title'].str.lower()

        if new_movie in cinemas['title'].values:
            # Find the cluster number of the input movie
            movie_cluster = cinemas.loc[cinemas['title'] == new_movie, 'cluster'].iloc[0]

            # Select a random movie from the same cluster
            recommended_movie = cinemas[cinemas['cluster'] == movie_cluster].sample()
            recommended_title = recommended_movie['title'].values[0]

            # Get TMDb details of the recommended movie
            movie_details = get_movie_details(recommended_title, api_key)
            if movie_details:
                # Construct TMDb URL for the movie
                tmdb_url = f"https://www.themoviedb.org/movie/{movie_details['id']}"
                return recommended_title, tmdb_url
            else:
                return 'No Recommendation'
        else:
            return 'No Recommendation'

    # Input your TMDb API key
    tmdb_api_key = "8036c981efcb468745e2b0e070a4177e"

    # Take movie input from the user
    new_movie = st.text_input("Enter movie:")

    # Recommend a movie based on the input and redirect to TMDb details
    if st.button("Recommend"):
        recommended_movie, tmdb_url = recommend_movie(new_movie, cinemas, tmdb_api_key)
        if recommended_movie != 'No Recommendation':
            st.write("Recommended movie:", recommended_movie)
            st.write("TMDb URL:", tmdb_url)
        else:
            st.write("No Recommendation")

ml()
