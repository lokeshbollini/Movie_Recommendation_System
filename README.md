# Movie_Recommendation_System

# Overview
The goal of this project is to recommend movies similar to a selected movie using a similarity matrix. The similarity matrix is stored as a pickle (.pkl) file and contains cosine similarity scores between movies. When a user selects a movie from the dropdown, the system returns the top recommendations based on these scores.

# Key components:

Pandas: Used for data manipulation and handling the similarity matrix.
Pickle: Used to load the precomputed similarity matrix.
Gradio: Provides an interactive web interface to interact with the recommendation system.

**How It Works**
Loading the Similarity Matrix:
The script begins by loading a precomputed movie similarity matrix from the file updatedmodel.pkl using the pickle module. This matrix is a Pandas DataFrame where both the index and columns represent movie titles, and the values represent cosine similarity scores between the movies.

# Recommendation Function:
The recommend_movies function takes two parameters:

movie_title: The title of the movie selected by the user.
num_recommendations: The number of movie recommendations to return (default is 5).

It checks if the selected movie exists in the DataFrame. If not, it returns an error message. Otherwise, it sorts the similarity scores for the selected movie in descending order and returns the top recommendations (skipping the first one, which is the movie itself).

# Gradio Interface:

Gradio is used to build a user-friendly web interface. The interface consists of:

A dropdown menu populated with movie titles from the similarity matrix.
A text output area that displays the recommended movies.
A title, description, and article note (crediting the developer).

# Launching the App:

Finally, the application is launched using Gradio's launch() method, which opens up the interface in your default web browser.
To run the movie recommendation system, simply execute the Python script:
python app.py
This will start a local Gradio server and provide a URL where you can access the recommendation system.

