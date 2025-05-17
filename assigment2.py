from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- Similarity Functions ---


def smc(sensor1, sensor2):
    count_same = sum(1 for i in range(len(sensor1)) if sensor1[i] == sensor2[i])
    return count_same / len(sensor1)


def jaccard(sensor1, sensor2):
    both_ones = sum(
        1 for i in range(len(sensor1)) if sensor1[i] == 1 and sensor2[i] == 1
    )
    at_least_one = sum(
        1 for i in range(len(sensor1)) if sensor1[i] == 1 or sensor2[i] == 1
    )
    return both_ones / at_least_one if at_least_one != 0 else 0


def cosine_sim(sensor1, sensor2):
    # Convert to 2D numpy arrays for sklearn
    vec1 = np.array(sensor1).reshape(1, -1)
    vec2 = np.array(sensor2).reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]


# --- Sensor Readings (0 = no event, 1 = event) ---

sensor_data = [
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # Sensor A
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],  # Sensor B
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1],  # Sensor C
]

new_sensor = [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]

sensor_names = ["Sensor A", "Sensor B", "Sensor C"]

# --- Weights ---

weight_smc = 0.3
weight_jaccard = 0.3
weight_cosine = 0.4

# --- Compute and Display Weighted Similarities ---

all_scores = []
for i, old_sensor in enumerate(sensor_data):
    sim_smc = smc(new_sensor, old_sensor)
    sim_jaccard = jaccard(new_sensor, old_sensor)
    sim_cos = cosine_sim(new_sensor, old_sensor)
    weighted_score = (
        (weight_smc * sim_smc)
        + (weight_jaccard * sim_jaccard)
        + (weight_cosine * sim_cos)
    )

    all_scores.append((sensor_names[i], weighted_score))
    print(
        f"{sensor_names[i]} -> SMC: {sim_smc:.2f}, Jaccard: {sim_jaccard:.2f}, Cosine: {sim_cos:.2f}, Weighted: {weighted_score:.3f}"
    )

# --- Find Most Similar Sensor ---

most_similar = max(all_scores, key=lambda x: x[1])
print(
    f"\nMost similar sensor to the new one is: {most_similar[0]} (Score = {most_similar[1]:.3f})"
)
