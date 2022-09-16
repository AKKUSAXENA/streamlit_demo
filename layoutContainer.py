import streamlit as st
import pandas as pd
import numpy as np

add_selectbox =  st.sidebar.selectbox(
    "How would you like to be conatacted?",
    ('Email','Home Phone','Mobile Phone')
)

# using st.columns
col1, col2 = st.columns(2)

with col1:

     st.header("A CAT")
     st.image("D:\\Streamlit\\1.jpg")

with col1:

     st.header("A CAT")
     st.image("D:\\Streamlit\\2.jpg")

# st.expander

st.line_chart({"data":[1,5,2,6,2,1]})

with st.expander("See explanation"):
    st.write("""
          The chart above shows some numbers i picked for you.
          I rolled actual dice for thses , so they're gauranteed to be random. 
    """)
    st.image("D:\Streamlit\streamlit_demo\\dice.jpg")

with st.container():
     st.write("This is inside the container")

     # you can call any streamlit command ,including 
     st.bar_chart(np.random.randn(50,3))

st.write("This is outside the container")