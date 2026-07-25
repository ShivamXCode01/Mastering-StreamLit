import streamlit as st

st.title("Language Picker")

st.subheader("Welcome to my first Website ")

Lang=st.selectbox("Select Your Language from the Below List: ",["C","C++","JAVA","Python","JavaScript","kotlin"])

st.write(f"You selected {Lang}")
st.success("Excellent Choice ! You selected Successfully")

