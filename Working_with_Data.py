import streamlit as st
import pandas as pd

st.title("Working with Data ")

st.subheader("We can work with multiple format or types of data in the streamlit ")

file=st.file_uploader("Upload your csv file" , type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file :
    st.subheader("Summary Stats :")
    st.write(df.describe())

# we can perform multiple features of pandas in streamlit directly because
# streamlit supports pandas