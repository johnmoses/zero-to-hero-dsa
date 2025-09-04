# Real World Application - Recommendation System (Simple collaborative filtering example)

import numpy as np

# User-item ratings matrix (users x items)
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
    [0, 1, 5, 4],
])

def cosine_similarity(vec1, vec2):
    num = np.dot(vec1, vec2)
    den = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return num / den if den else 0

def recommend(user_idx, ratings, top_n=2):
    similarities = []
    for i in range(ratings.shape[0]):
        if i != user_idx:
            sim = cosine_similarity(ratings[user_idx], ratings[i])
            similarities.append((i, sim))
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Aggregate ratings from most similar users
    # This should be a 1D vector of scores, not a matrix.
    weighted_scores = np.zeros(ratings.shape[1])
    total_sim = 0
    for i, sim in similarities[:top_n]:
        # Ensure similarity is positive before weighting
        if sim > 0:
            weighted_scores += sim * ratings[i]
            total_sim += sim
    
    if total_sim > 0:
        weighted_scores /= total_sim

    # Recommend items not yet rated by user
    user_ratings = ratings[user_idx]
    recommendations = []
    for idx, score in enumerate(weighted_scores):
        if user_ratings[idx] == 0 and score > 0:
            recommendations.append((idx, score))
            
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

if __name__ == "__main__":
    user = 0
    recs = recommend(user, ratings)
    print(f"Recommendations for user {user}: {recs}")