import streamlit as st
import cv2

# This is the homepage of the website

# Set Page Config -> title, logo, layout (centred by default)
st.set_page_config(
    page_title="Float n Pose", 
    page_icon="🪐"
)

# Used to remove the streamlit branding
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/styles.css")

st.title(":blue[Float n Pose]")

def leaderboard() :
    # Dummy Leaderboard Data - initialise to empty dictionary when
    # Contains in form of key value pairs of username and score 
    # To Do - store it in a panda data frame and then display it after sorting
    leaderboard = {
        "User1": 10,
        "User2": 20,
        "User3": 40,
        "User4": 5,
        "User5": 60,
    }

    sortedLeaderBoard = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)

    st.header("Leaderboard")

    # Print the leaderboard
    for user in sortedLeaderBoard :
        # st.write(user + ": " + str(leaderboard[user]))
        cols = st.columns(2)
        cols[0].write(user[0])
        cols[1].write(str(user[1]))



def webcam() :

    st.header("Webcam")
    
    # Initialise cap - Captures video frames from webcam 0. 
    cap = cv2.VideoCapture(0)

    # Empty Frame for storing webcam feed. 
    frame_placeholder = st.empty()

    # button to stop the feed - change later
    stop_button_pressed = st.button("Stop")

    # Feed is accessed till in this loop
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()

        # End the Video Capture
        if not ret:
            st.write("Video Capture Ended")
            break
        
        # convert to RGB format - supported by streamlit and display it
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")

        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
    
    # release and destroy (destructor)
    cap.release()
    cv2.destroyAllWindows()


# Webcam Test
def main() :
    col1, col2 = st.columns([4, 2], gap="large", vertical_alignment="center")

    with col2 :
        leaderboard()
    
    with col1 :
        webcam()


if __name__ == "__main__" :
    main()