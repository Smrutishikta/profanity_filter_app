import pandas as pd
import numpy as np
import streamlit as st
import pickle 
from better_profanity import profanity
from profanity_check import predict, predict_prob
profanity.load_censor_words()

add_selectbox = st.sidebar.selectbox('What would you like to check?',('Text', 'Image', 'Handwriting'))

st.title("Profanity filter")
x = st.text_input("Text","Type here")

if st.button("Check"):
    result=profanity.censor(x)
    st.success("The oput is: {}".format(result))
    predict=predict_prob([x])
    st.success("Toxicity score: {}".format(predict))

