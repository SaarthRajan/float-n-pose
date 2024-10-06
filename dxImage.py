# import cv2
# import mediapipe as mp
# import numpy as np
# import streamlit as st
# from sklearn.metrics.pairwise import cosine_similarity

# # Initialize Mediapipe pose object
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose()

# # Function to extract keypoints from an image
# def extract_keypoints(image):
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = pose.process(image_rgb)
#     if results.pose_landmarks:
#         keypoints = []
#         for lm in results.pose_landmarks.landmark:
#             keypoints.append([lm.x, lm.y, lm.z])
#         return np.array(keypoints)
#     else:
#         return None

# # Function to calculate cosine similarity between two sets of keypoints
# def cosine_similarity_keypoints(keypoints1, keypoints2):
#     if keypoints1 is not None and keypoints2 is not None:
#         return cosine_similarity([keypoints1.flatten()], [keypoints2.flatten()])[0][0]
#     else:
#         return None

# # Function to calculate the score based on similarity percentage
# def calculate_score(similarity_percentage):
#     if similarity_percentage >= 98:
#         return 5
#     elif similarity_percentage < 90:
#         return 0
#     else:
#         return round((similarity_percentage - 90) / 2)  # Score between 0 and 5 for 90-98 range

# # Streamlit app
# st.title("Pose Similarity Checker / Float n' Pose")

# # Upload two images
# uploaded_file1 = "images/host.jpg"
# uploaded_file2 = st.file_uploader("Upload Second Image", type=["jpg", "jpeg", "png"])

# if uploaded_file1 and uploaded_file2:
#     # Convert uploaded files to OpenCV images
#     file_bytes1 = np.asarray(bytearray(uploaded_file1.read()), dtype=np.uint8)
#     file_bytes2 = np.asarray(bytearray(uploaded_file2.read()), dtype=np.uint8)
    
#     image1 = cv2.imdecode(file_bytes1, 1)
#     image2 = cv2.imdecode(file_bytes2, 1)
    
#     st.image([image1, image2], caption=["Host photo", "Player's Pose"], width=300)

#     # Extract keypoints from both images
#     keypoints1 = extract_keypoints(image1)
#     keypoints2 = extract_keypoints(image2)

#     # Check if keypoints were detected
#     if keypoints1 is not None and keypoints2 is not None:
#         # Calculate cosine similarity
#         similarity_score = cosine_similarity_keypoints(keypoints1, keypoints2)
        
#         if similarity_score is not None:
#             similarity_percentage = similarity_score * 100
#             score = calculate_score(similarity_percentage)
#             st.success(f"Pose Similarity: {similarity_percentage:.2f}%")
#             st.info(f"Pose Comparison Score: {score}/5")
#         else:
#             st.error("Could not calculate similarity. Make sure poses are detected correctly.")
#     else:
#         st.error("Pose not detected in one or both images. Try different images.")

# def compare_two_images(host_path, image_path):

#     # Convert uploaded files to OpenCV images
#     file_bytes1 = np.asarray(bytearray(uploaded_file1.read()), dtype=np.uint8)
#     file_bytes2 = np.asarray(bytearray(uploaded_file2.read()), dtype=np.uint8)
    
#     image1 = cv2.imdecode(file_bytes1, 1)
#     image2 = cv2.imdecode(file_bytes2, 1)
    
#     st.image([image1, image2], caption=["Host photo", "Player's Pose"], width=300)

#     # Extract keypoints from both images
#     keypoints1 = extract_keypoints(image1)
#     keypoints2 = extract_keypoints(image2)

#     # Check if keypoints were detected
#     if keypoints1 is not None and keypoints2 is not None:
#         # Calculate cosine similarity
#         similarity_score = cosine_similarity_keypoints(keypoints1, keypoints2)
        
#         if similarity_score is not None:
#             similarity_percentage = similarity_score * 100
#             score = calculate_score(similarity_percentage)
#             st.success(f"Pose Similarity: {similarity_percentage:.2f}%")
#             st.info(f"Pose Comparison Score: {score}/5")
#         else:
#             st.error("Could not calculate similarity. Make sure poses are detected correctly.")
#     else:
#         st.error("Pose not detected in one or both images. Try different images.")





import os
import cv2
import mediapipe as mp
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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

# Example usage
if __name__ == "__main__":
    player_scores = score_players_images()
    for player, data in player_scores.items():
        print(f"Image: {player}, Similarity: {data['similarity_percentage']}%, Score: {data['score']}/5")
