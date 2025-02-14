# Overview
This repository contains a Movie Recommendation System that suggests movies based on user-selected movie titles. The recommendation is powered by cosine similarity, computed using user rating data from the MovieLens dataset.

# Dataset
The dataset used is ml-latest-small from GroupLens. It contains:
100,836 ratings and 3,683 tag applications
9,742 movies rated by 610 users
Data collected between March 29, 1996, and September 24, 2018

# Project Structure
- The repository includes the following files:
- Movies_sim_df.py
- Loads the ratings.csv and movies.csv datasets
- Cleans the data and merges ratings with movie titles
- Creates a user-movie matrix
- Computes the cosine similarity matrix for movies
- Saves the similarity matrix as updatedmodel.pkl
- app.py (Main Gradio application)
- Loads the precomputed movie similarity matrix from updatedmodel.pkl
- Implements a Gradio-based interface for movie recommendations
- Allows users to select a movie and get similar movie recommendations

## How It Works:

# Model Training (Movies_sim_df.py)
- The script loads the MovieLens dataset, cleaning and merging ratings.csv and movies.csv.
- It constructs a user-movie rating matrix, where each row represents a user and each column represents a movie.
- Missing ratings are replaced with 0 to ensure a complete dataset.
- Using cosine similarity, the system calculates how similar each movie is to the others.
- The similarity matrix is stored as updatedmodel.pkl for later use.
# Gradio Interface (app.py)
- Loads the precomputed similarity matrix from updatedmodel.pkl.
- Displays a dropdown menu for users to select a movie.
- Once a movie is selected, it retrieves the top n most similar movies using cosine similarity.
- Displays the recommendations in a simple text output.

# Example Usage
- Select a movie from the dropdown.
- The system will recommend 5 similar movies based on cosine similarity.
- The recommendations update dynamically when a different movie is selected.

# Dependencies
- pandas (Data processing)
- numpy (Numerical computations)
- scikit-learn (Cosine similarity calculation)
- gradio (Interactive UI for recommendations)
