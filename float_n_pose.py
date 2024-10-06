import streamlit as st
import cv2
import os
import time
import tempfile

# pg = st.navigation([st.Page("pages\confirm_image.py")], position="hidden")

# Set Page Config -> title, logo, layout (centred by default)
st.set_page_config(
    page_title="Float n Pose", 
    page_icon="🪐",
    initial_sidebar_state="collapsed"
)

# Used to remove the streamlit branding
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/styles.css")

st.title(":blue[Float n Pose]")

# Dummy Leaderboard Data - initialise to empty dictionary when
# Contains in form of key value pairs of username and score 
# To Do - store it in a panda data frame and then display it after sorting
leaderboard_dict = {
    "User1": 10,
    "User2": 20,
    "User3": 40,
    "User4": 5,
    "User5": 60,
}

image_directory = "./images"
image_path = "./images/temp.png"
image_name = "temp.png"

def leaderboard() :

    sortedLeaderBoard = sorted(leaderboard_dict.items(), key=lambda x:x[1], reverse=True)

    st.header("Leaderboard")

    # Print the leaderboard
    for user in sortedLeaderBoard :
        # st.write(user + ": " + str(leaderboard[user]))
        cols = st.columns(2)
        cols[0].write(user[0])
        cols[1].write(str(user[1]))

def countdown():
    with st.empty() :
        for i in range(1, 4) :
            st.header(str(i))
            time.sleep(1)

def webcam() :

    captured = False

    st.header("Webcam")
    
    # Initialise cap - Captures video frames from webcam 0. 
    cap = cv2.VideoCapture(0)

    # Empty Frame for storing webcam feed. 
    frame_placeholder = st.empty()

    # Capture Button
    capture_button = st.button("Capture")

    # Feed is accessed till in this loop
    while cap.isOpened():

        # if os.path.exists(image_path):
        #     # os.remove(image_path)
        #     os.unlink(image_path)

        
        ret, frame = cap.read()

        # End the Video Capture
        if not ret:
            st.write("Video Capture Ended")
            break
        
        # convert to RGB format - supported by streamlit and display it
        frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_new)

        if capture_button :

            countdown()

            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix='.png').name

            if cv2.imwrite(temp_image_path, frame) :
                if os.path.exists(image_path) :
                    os.remove(image_path)
                    time.sleep(0.1)

                os.rename(temp_image_path, image_path)
                captured = True
                break
            else :
                st.write("There was an error, Kindly try again")


            # if os.path.exists(image_path):
            #     # os.remove(image_path)
            #     os.unlink(image_path)

            # cv2.imwrite(image_path, frame)

        # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break
    
    # release and destroy (destructor)
    cap.release()
    cv2.destroyAllWindows()

    if captured :
        st.switch_page("pages/confirm_image.py")


# Webcam Test
def main() :
    col1, col2 = st.columns([2, 1], gap="large", vertical_alignment="center")

    with col2 :
        leaderboard()
    
    with col1 :
        webcam()


if __name__ == "__main__" :
    main()