import streamlit as st
import pandas as pd

# normal way
st.write("Hello **World**! ")

# magic command

"Hello **World**! "

# st.caption

st.caption("This is a string")

# st.code

code = '''
def hello():
    print("We are mechzookartz")
'''

st.code(code , language="Python")

# st.text
st.text("we are mechzookartz")
