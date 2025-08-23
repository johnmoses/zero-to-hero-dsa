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
    weighted_ratings = np.zeros(ratings.shape)
    total_sim = 0
    for i, sim in similarities[:top_n]:
        weighted_ratings += sim * ratings[i]
        total_sim += sim
    weighted_ratings /= total_sim if total_sim else 1

    # Recommend items not yet rated by user
    user_ratings = ratings[user_idx]
    recommendations = [(idx, score) for idx, score in enumerate(weighted_ratings) if user_ratings[idx] == 0]
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

if __name__ == "__main__":
    user = 0
    recs = recommend(user, ratings)
    print(f"Recommendations for user {user}: {recs}")
