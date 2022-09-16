import streamlit as st

# adding audio 
audio_file = open('D:\\Streamlit\\streamlit_demo\\audio.ogg','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/ogg')

# adding video file video.mp4

video_file = open('D:\\Streamlit\\streamlit_demo\\video.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes)

# adding video file vid.mp4

video_file1 = open('D:\\Streamlit\\streamlit_demo\\vid.mp4','rb')
video_bytes1 = video_file1.read()

st.video(video_bytes1)

