import streamlit as st
import os
import time
from info import leaderboard_dict
import info

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


def slideshow():

    image_directory = "./images/"
    
    for image in os.listdir(image_directory) :
        st.image(f"{image_directory}{image}")
        time.sleep(1)
    
        

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

def main():

    cols = st.columns(2)
    with cols[1] :
        leaderboard()
        play_again = st.button("Play Again", type="secondary")

    with cols[0] :
        with st.empty():
            while True :
                slideshow()
                if play_again :
                    info.theme = ""
                    st.switch_page("float_n_pose.py")


if __name__ == '__main__':
    st.title("Results")
    main()