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

image_directory = "./images"

def confirmImage(path):

    # Page headings
    st.title(":blue[Float n Pose]")
    st.header("Do you want to upload this?")

    # initialise 2 columns with ration 3:2
    cols = st.columns([3, 2], gap="large")

    # displays image located at the path
    with cols[0] :
        # if st.image(path) :
        #     st.image(path)
        # else :
        #     st.image("./images/Sample.png")
        st.image("./images/temp.png", channels="BGR")

    # displays the details the user has to enter
    with cols[1] :
        username = st.text_input("Enter Your Name Here")
        insideColumns = st.columns(2)
        with insideColumns[0] :
            confirm_button = st.button("Confirm")
        with insideColumns[1] :
            retake_button = st.button("Retake")

        # Actions after button is pushed - Subject to Change

        if confirm_button :
            if username :
                st.write(f"Username is {username}")
                # st.switch_page("float-n-pose.py")
            else :
                st.write("Kindly Enter the username")
        elif retake_button:
            st.write("You are not choosing this image")
            # os.chdir(image_directory)
            # os.remove("temp.jpg")
            # st.switch_page("float-n-pose.py")

        # while (not confirm_button and not retake_button):
        #     if confirm_button :
        #         if username :
        #             st.write(f"Username is {username}")
        #             st.switch_page("float-n-pose.py")
        #         else :
        #             st.write("Kindly Enter the username")
        #     elif retake_button:
        #         os.chdir(image_directory)
        #         os.remove("temp.jpg")
        #         st.switch_page("float-n-pose.py")
        


confirmImage("images/temp.png")