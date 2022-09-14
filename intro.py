# import the necessary modules
# 
import streamlit as st 
import pandas as pd

# Adding titles

st.title("Hello, Welcome to Mechzookartz")

# header
st.header("This is a header") 

# adding sub headers
st.subheader("This is a subheader")

Data = {
    "Company":["google","Apple","Ineuwron","Samsung"],
    "price": ["100","200","300","400"],
    "Language": [ "Python","Jave","C++","julian"]
}

st.write(Data)

st.write(pd.DataFrame(Data))

# Mrkdown

st.markdown("""This is  a markdown file
# h1 tag
## h2 tag
### h3 tag
""")