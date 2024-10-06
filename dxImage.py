import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
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

# Streamlit app
st.title("Pose Similarity Checker / Float n' Pose")

# Upload two images
uploaded_file1 = st.file_uploader("Upload First Image", type=["jpg", "jpeg", "png"])
uploaded_file2 = st.file_uploader("Upload Second Image", type=["jpg", "jpeg", "png"])

if uploaded_file1 and uploaded_file2:
    # Convert uploaded files to OpenCV images
    file_bytes1 = np.asarray(bytearray(uploaded_file1.read()), dtype=np.uint8)
    file_bytes2 = np.asarray(bytearray(uploaded_file2.read()), dtype=np.uint8)
    
    image1 = cv2.imdecode(file_bytes1, 1)
    image2 = cv2.imdecode(file_bytes2, 1)
    
    st.image([image1, image2], caption=["Host photo", "Player's Pose"], width=300)

    # Extract keypoints from both images
    keypoints1 = extract_keypoints(image1)
    keypoints2 = extract_keypoints(image2)

    # Check if keypoints were detected
    if keypoints1 is not None and keypoints2 is not None:
        # Calculate cosine similarity
        similarity_score = cosine_similarity_keypoints(keypoints1, keypoints2)
        
        if similarity_score is not None:
            similarity_percentage = similarity_score * 100
            score = calculate_score(similarity_percentage)
            st.success(f"Pose Similarity: {similarity_percentage:.2f}%")
            st.info(f"Pose Comparison Score: {score}/5")
        else:
            st.error("Could not calculate similarity. Make sure poses are detected correctly.")
    else:
        st.error("Pose not detected in one or both images. Try different images.")
