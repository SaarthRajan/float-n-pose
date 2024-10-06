import streamlit as st
import os
import time
import shutil
import tempfile
from info import leaderboard_dict
import info

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

image_directory = "./images/"

# to center the image
cols = st.columns(4)
with cols[1]:
    # space apps logo
    st.image("./space_apps_logo.png", width=300)

st.title(":blue[Float n Pose 🧑🏼‍🚀]")
st.header("Do you want to upload this?")

def confirmImage(path):
    
    username = ""
        
    # initialise 2 columns with ration 3:2
    cols = st.columns([3, 2], gap="large")

    # displays image located at the path
    with cols[0] :
        with st.empty() :
            st.image(path, channels="RGB")
        

    # displays the details the user has to enter
    with cols[1] :
        if info.theme == "" :
            username = "host"
            hint = st.text_input("Give a hint to other players")
            info.theme = hint
        else :
            username = st.text_input("Enter Your Name Here")

        insideColumns = st.columns(2)
        with insideColumns[0] :
            retake_button = st.button("Retake", type="secondary")
        with insideColumns[1] :
            confirm_button = st.button("Confirm", type="primary")

        # Actions after button is pushed
        if confirm_button :
            if username and info.theme:
                st.write(f"Username is {username}")
                temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg').name
                shutil.move(path, temp_image_path)
                os.rename(temp_image_path, f"{image_directory}{username}.jpg")

                if username not in leaderboard_dict :
                    leaderboard_dict[username] = 0 # initialise leaderboard

                st.switch_page("float_n_pose.py")

            else :
                st.write("Kindly Enter the username and/or hint")

        if retake_button:

            st.write("You are not choosing this image")
            
            if os.path.exists(path):
                os.remove(path)
                time.sleep(0.1)
            
            st.switch_page("float_n_pose.py")

        


confirmImage("./images/temp.jpg")