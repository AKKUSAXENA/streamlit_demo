from statistics import variance
import numpy as np
import pandas as pd
import pickle
import streamlit as st

from PIL import Image

# app = Flask(__name__)
# swagger(App)

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

# @app.route('/')
def Welcome():
    return "Welcome All"

# @app.route('/predict',methods = ["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    """Lets Authenticate the Banks Note This is using docstrings for specification.
    ---
    parameters:
        -name: variance
        in = query
        type = number
        required :true
        name: skewness
        in:query
        type =number
        required:true
        name = entropy
        in:query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style ="color:white:text-align:center;">Streamlit Bank Authentictor ML app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("varince","Type Here")
    skewness=st.text_input("skewness","Type Here")
    curtosis=st.text_input("curtosis","Type Here")
    entropy=st.text_input("entropy","Type Here")
    result=""

    if st.button("predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("lets Learn")
        st.text("Built with streamlit")

if __name__ == '__main__':
    main()
