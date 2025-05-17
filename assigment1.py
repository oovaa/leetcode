from sklearn.metrics import mutual_info_score
import numpy as np

# --- Similarity Functions ---


def similarity_smc(user1, user2):
    similar_count = 0
    for i in range(len(user1)):
        if user1[i] == user2[i]:
            similar_count += 1
    return similar_count / len(user1)


def similarity_jaccard(user1, user2):
    both_like = 0
    at_least_one = 0
    for i in range(len(user1)):
        if user1[i] == 1 or user2[i] == 1:
            at_least_one += 1
            if user1[i] == 1 and user2[i] == 1:
                both_like += 1
    return both_like / at_least_one if at_least_one != 0 else 0


def similarity_mutual_info(user1, user2):
    return mutual_info_score(user1, user2)


# --- Users' Movie Preferences ---

movie_preferences = [
    [1, 1, 0, 0, 1],  # User 1
    [0, 1, 1, 1, 0],  # User 2
    [1, 0, 0, 1, 1],  # User 3
]

new_user_prefs = [1, 1, 0, 0, 0]  # New user

movie_labels = ["Action", "Drama", "Comedy", "Horror", "Sci-fi"]

# --- Weights for Each Similarity Metric ---

weight_smc = 0.3
weight_jaccard = 0.3
weight_mi = 0.4

# --- Calculate Weighted Similarities ---

all_similarities = []
for index, other_user in enumerate(movie_preferences):
    score_smc = similarity_smc(new_user_prefs, other_user)
    score_jaccard = similarity_jaccard(new_user_prefs, other_user)
    score_mi = similarity_mutual_info(new_user_prefs, other_user)
    weighted_score = (
        (weight_smc * score_smc)
        + (weight_jaccard * score_jaccard)
        + (weight_mi * score_mi)
    )

    all_similarities.append((index + 1, weighted_score, other_user))
    print(
        f"User {index+1}: SMC = {score_smc:.2f}, Jaccard = {score_jaccard:.2f}, MI = {score_mi:.2f}, Weighted Score = {weighted_score:.3f}"
    )

# --- Find the Most Similar User ---

most_similar_user = max(all_similarities, key=lambda x: x[1])
user_id = most_similar_user[0]
user_profile = most_similar_user[2]
print(f"\nMost similar user is User {user_id} (Score = {most_similar_user[1]:.3f})")

# --- Recommend Movies ---

print("Recommended movies based on similar user's preferences:")
for i in range(len(user_profile)):
    if user_profile[i] == 1 and new_user_prefs[i] == 0:
        print("-", movie_labels[i])
