# Float n Pose - Created in 36 hours
Created for Nasa Space Apps Challenge 2024 (E7, University of Waterloo)

## Team Members
Saarth, Rishi, Seth and Rithika

## Summary
We developed Float n Pose, a game that is setup on a laptop or device with a camera where astronauts can compete by capturing an image of themselves posing in a way that they think most closely resembles the host's prompt. At the end of the game, the astronauts' poses would be compared to the host's pose to determine which poses most closely matched. This addresses physical, mental, and social well-being challenges when living in a microgravity environment by encouraging the astronauts to move and stretch their bodies as well as share their cultures and interests in a fun and entertaining way.

## Tech Used
Streamlit for UI. 
OpenCV for Webcam and Image input. 
MediaPipe for Pose Comparison. 

## Setup

### 1. Git Clone
Clone the repository in your local machine using the following command

git clone https://github.com/SaarthRajan/float-n-pose.git

### 2. Install requirements
Go into the float-n-pose directory and install the requirements using the following command

pip install -r requirements.txt

### 3. To run the app, use the following command

streamlit run float_n_pose.py

## How to Play
For this game, one person will act as a host and strike a pose by leveraging the microgravity environment. They will then input a hint for the other astronauts to strike a similar pose. 
You can play it asynchronously by submitting a photo any time of the day and compare it once everyone has submitted.
Game ends when the End Game button is clicked. It shows a slideshow of all the poses along with a leaderboard. Our application then uses OpenCV and MediaPipe to compare the poses and give a score out on a scale of 1 to 5.

## Note:
To avoid bugs, if you are prompted to enter username and you are a host, enter "host" as the username. Since this software was developed within 36 hours, the feature of scoring is not as accurate as we would have liked it to be. 
