import streamlit as st
import pandas as pd
import numpy as np

# st.stop
# streamlit will not run any statements after st.stop(). we recommend rendering a message to explain 
# script has stopped. when run outside of streamlit, this will raise an exception.

name = st.text_input("Name")
if not name:
    st.warning("Please input a name.")
    st.stop()
st.success("Thank ypu for inputting a name.")

# st.form

# Inserting elements using "with" notation:
with st.form("my form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("form checkbox")

    # every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider",slider_val,"Checkbox",checkbox_val)
st.write("outside the form")