import streamlit as st
import cv2
import os
import time
import numpy as np
from info import leaderboard_dict
from info import theme


# pg = st.navigation([st.Page("pages\confirm_image.py")], position="hidden")

# Set Page Config -> title, logo, layout (centred by default)
st.set_page_config(
    page_title="Float n Pose", 
    page_icon="🪐",
    initial_sidebar_state="collapsed" # hiding the sidebar
)

# Used to remove the streamlit branding - and format other stuff (also check configure.toml for theme)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/styles.css")

# to center the image
cols = st.columns(4)
with cols[1]:
    # space apps logo
    st.image("./space_apps_logo.png", width=300)

st.title(":blue[Float n Pose 🧑🏼‍🚀]")

image_directory = "./images"
image_path = "./images/temp.jpg"

def leaderboard() :

    # sort in decreasing order based on their scores
    sortedLeaderBoard = sorted(leaderboard_dict.items(), key=lambda x:x[1], reverse=True)

    st.header("Leaderboard")

    # Print the leaderboard in table format
    for user in sortedLeaderBoard :
        # st.write(user + ": " + str(leaderboard[user]))
        cols = st.columns(2)
        cols[0].write(user[0])
        cols[1].write(str(user[1]))

# Currently: Countdown for error handling - will later implement it for countdown before capture
def countdown():
    with st.empty() :
        for i in range(1, 4) :
            st.header(str(4 - i))
            time.sleep(0.7)

def webcam() :
    # bool when captured
    captured = False

    st.header("Webcam")

    if theme:
        st.header(f"The pose of the day is {theme}")
    else :
        st.write("To start the game, capture a photo")
    
    # Initialise cap - Captures video frames from webcam 0. 
    cap = cv2.VideoCapture(0)

    # Empty Frame for storing webcam feed. 
    frame_placeholder = st.empty()

    # Capture Button
    capture_button = st.button("Capture", type="primary")

    st.write("If the image is not rendered properly, click on capture again :)")

    # Feed is accessed till in this loop
    while cap.isOpened():
        
        ret, frame = cap.read()

        # End the Video Capture
        if not ret:
            st.write("Video Capture Ended")
            break
        
        # convert to RGB format - supported by streamlit and display it
        frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_new)

        if capture_button :

            countdown() # for errors

            # to brighten the image
            intensity = np.ones(frame.shape, dtype="uint8") * 60
            image_bright = cv2.add(frame, intensity)

            # write to image path
            cv2.imwrite(image_path, image_bright)

            captured = True

            break
    
    # release and destroy (destructor)
    cap.release()
    cv2.destroyAllWindows()

    if captured :
        st.switch_page("pages/confirm_image.py")


# Webcam Test
def main() :
    col1, col2 = st.columns([2, 1], gap="large") #, vertical_alignment="center"

    with col2 :
        leaderboard()
    
    with col1 :
        webcam()


if __name__ == "__main__" :
    main()