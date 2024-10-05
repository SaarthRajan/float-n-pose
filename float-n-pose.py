import streamlit as st

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
local_css("styles/styles.css")

st.title("Float n Pose")