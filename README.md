Overview

This repository contains a Movie Recommendation System that suggests movies based on user-selected movie titles. The recommendation is powered by cosine similarity, computed using user rating data from the MovieLens dataset.

Dataset

The dataset used is ml-latest-small from GroupLens. It contains:

100,836 ratings and 3,683 tag applications

9,742 movies rated by 610 users

Data collected between March 29, 1996, and September 24, 2018

Project Structure

The repository includes the following files:

Movies_sim_df.py

Loads the ratings.csv and movies.csv datasets

Cleans the data and merges ratings with movie titles

Creates a user-movie matrix

Computes the cosine similarity matrix for movies

Saves the similarity matrix as updatedmodel.pkl

app.py (Main Gradio application)

Loads the precomputed movie similarity matrix from updatedmodel.pkl

Implements a Gradio-based interface for movie recommendations

Allows users to select a movie and get similar movie recommendations
