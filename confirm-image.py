import streamlit as st

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

def confirmImage(path):

    st.title(":blue[Float n Pose]")

    st.header("Do you want to upload this?")

    cols = st.columns([3, 2], gap="large")

    with cols[0] :
        st.image(path)

    with cols[1] :
        username = st.text_input("Enter Your Name Here")
        insideColumns = st.columns(2)
        with insideColumns[0] :
            confirm_button = st.button("Confirm")
        with insideColumns[1] :
            retake_button = st.button("Retake")

        if confirm_button :
            if username :
                st.write(f"Username is {username}")
            else :
                st.write("Kindly Enter the username")
        elif retake_button:
            st.write("You decided not to go for the photo")


confirmImage("images/Sample.png")