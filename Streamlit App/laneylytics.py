from git import Head
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


with header:
    st.title('Laney Media Analytics Dashboard')
    

with dataset:
    st.header('Content Plan Dataset')
    st.text(' test test test')

    #clickup_data = pd.read_csv('')
    #st.write(clickup_data.head())

with features:
    st.header('Best Preforming Content')



with model_training:
    st.header('Predicting Views')
