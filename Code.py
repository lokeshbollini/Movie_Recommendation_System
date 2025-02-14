import pandas as pd
import pickle
import gradio as gr

# Load the precomputed movie similarity matrix from the .pkl file
with open("updatedmodel.pkl", "rb") as file:
    movie_sim_df = pickle.load(file)

# Gradio function for movie recommendation
def recommend_movies(movie_title, num_recommendations=5):
    """Returns a list of recommended movies based on cosine similarity"""
    if movie_title not in movie_sim_df.index:
        return f"Movie '{movie_title}' not found in dataset."
    
    similar_movies = movie_sim_df[movie_title].sort_values(ascending=False)[1:num_recommendations+1]
    return "\n".join(similar_movies.index.tolist())

# Gradio Interface
iface = gr.Interface(
    fn=recommend_movies,
    inputs=gr.Dropdown(choices=movie_sim_df.index.tolist(), label="Select a Movie"),
    outputs="text",
    title="Movie Recommendation System",
    description="Select a movie and get recommendations using **cosine similarity**.",
    article="Developed by Lokesh Bollini"
)

# Launch the app
iface.launch()
