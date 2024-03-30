# Final_project

## Summary
This dataset (ml-25m) describes 5-star rating and free-text tagging activity from MovieLens, a movie recommendation service. It contains     25 000 095 ratings across 58 958 movies.This dataset was generated on November 21, 2019.

Users were selected at random for inclusion. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files genome-scores.csv, genome-tags.csv, links.csv, movies.csv, ratings.csv and tags.csv.

## Overview
After cleaning, the cinemas dataset contains information about various movies, including the number of ratings, title, average rating, year of release, and genre categories.

## Data Description
- **number_of_ratings**: The number of ratings received by the movie.
- **title**: The title of the movie.
- **genres**: The genres associated with the movie. 
- **rating**: The average rating of the movie.
- **year**: The year of release of the movie.
- **Action**, **Adventure**, **Animation**, **Children**, ..., **Western**: Binary indicators of whether the movie belongs to each genre category.
- **cluster**: A categorical variable indicating the cluster/group the movie belongs to.

## Features

- Recommends movies based on user input.
- Retrieves movie details from TMDb API.
- Displays recommendations with TMDb URLs for more information.

## Dependencies

- Python 
- numpy
- pandas
- streamlit 
- Pillow
- requests
- Tableau https://public.tableau.com/app/profile/alexandre.ghanzouri1300/viz/MovieDiscovery/MovieDiscoveryDashboard