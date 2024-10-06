import os
import cv2
import mediapipe as mp
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from info import leaderboard_dict

# Initialize Mediapipe pose object
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to extract keypoints from an image
def extract_keypoints(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks:
        keypoints = []
        for lm in results.pose_landmarks.landmark:
            keypoints.append([lm.x, lm.y, lm.z])
        return np.array(keypoints)
    else:
        return None

# Function to calculate cosine similarity between two sets of keypoints
def cosine_similarity_keypoints(keypoints1, keypoints2):
    if keypoints1 is not None and keypoints2 is not None:
        return cosine_similarity([keypoints1.flatten()], [keypoints2.flatten()])[0][0]
    else:
        return None

# Function to calculate the score based on similarity percentage
def calculate_score(similarity_percentage):
    if similarity_percentage >= 98:
        return 5
    elif similarity_percentage < 90:
        return 0
    else:
        return round((similarity_percentage - 90) / 2)  # Score between 0 and 5 for 90-98 range

# Generic function to score all player images
def score_players_images():
    # Path to the images folder and host image
    images_folder = "images/"
    host_image_path = os.path.join(images_folder, "host.jpg")

    # Load the host image and extract keypoints
    host_image = cv2.imread(host_image_path)
    host_keypoints = extract_keypoints(host_image)
    
    if host_keypoints is None:
        raise ValueError("Pose could not be detected in the host image.")

    # Initialize a dictionary to store scores
    player_scores = {}

    # Loop through all files in the images folder except host.jpg
    for image_file in os.listdir(images_folder):
        if image_file != "host.jpg" and image_file.endswith((".jpg")):
            player_image_path = os.path.join(images_folder, image_file)
            player_image = cv2.imread(player_image_path)
            player_keypoints = extract_keypoints(player_image)

            if player_keypoints is not None:
                similarity_score = cosine_similarity_keypoints(host_keypoints, player_keypoints)
                similarity_percentage = similarity_score * 100
                score = calculate_score(similarity_percentage)

                # Add the score to the dictionary
                player_scores[image_file] = {
                    "similarity_percentage": round(similarity_percentage, 2),
                    "score": score
                }

    return player_scores

def main():
    player_scores = score_players_images()
    for player, data in player_scores.items():
        entry = str(player[:-4])
        leaderboard_dict[entry] += int(data['score'] / 5)

# Example usage
if __name__ == "__main__":
    main()