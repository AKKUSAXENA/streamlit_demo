from datetime import datetime
from optparse import Option
import streamlit as st
import pandas as pd
import numpy as np

# # button  
# st.button("Hello We are mechzookartz") # to make a button named as hello we are mechzookartz


# button 
if st.button("Hello We are mechzookartz"):
    st.write("Lets buy Mrchzookartz")

else:
    st.write("Hello there")

# checkbox
agree = st.checkbox("I agree to buy a product") 

if agree:
    st.write("Welcome to mechzookartz")

# radio button

genre = st.radio(
    "What's your favourite movie",
    ("Drama","action movie")
)
if genre == "Drama":
    st.write("Its a drama movie")
else:
    st.write("Its a action movie")

# select box
Option = st.selectbox(
    "how would you like to be contacted?",
    ('Email','Home phone','Mobile phone')
)

st.write('You selected:',Option)

# multiselect

Options = st.multiselect(
    "What are your favourite colors?",
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)
st.write('You selected:',Options)

# sliders
age = st.slider('How old are you ?', 0 , 130 , 25)
st.write("I'm ",age ,"Years old")

# examples of range slider
values = st.slider(
    "Select a range of values",
    0.1,100.0, (25.0,75.0))
st.write("values",values)

# examples of date time slider

from datetime import datetime
start_time = st.slider(
    "when do you start?",
    value = datetime(2022, 1,1,9,30),
    format = "MM/DD/YY - hh:mm")
st.write("start_time:",start_time)