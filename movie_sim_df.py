import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load the ratings and movies datasets
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# Clean movie titles
movies['title'] = movies['title'].str.strip()

# Merge ratings with movie titles
df = ratings.merge(movies, on="movieId")

# Create user-item matrix
user_movie_matrix = df.pivot_table(index='userId', columns='title', values='rating', aggfunc='mean').fillna(0)

# Compute similarity matrix
movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_sim_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Save the model to a .pkl file
with open("updatedmodel.pkl", "wb") as file:
    pickle.dump(movie_sim_df, file)

print("Model saved as 'updatedmodel.pkl'")
