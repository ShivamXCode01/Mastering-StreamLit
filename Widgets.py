import streamlit as st 

st.title("Widgets")
st.subheader("In this we study about the widgets!")

# Button 
click=st.button("Learn Language")
if click:
    st.success("You learned the language successfully!")

# CheckBox 
st.write("Select your languages : ")
st.checkbox("C")
st.checkbox("C++")
st.checkbox("JAVA")
st.checkbox("PYTHON") 
st.checkbox("JavaScript")
st.checkbox("Kotlin")

# Radio Buttons
st.radio("Choose your Degree :",["B.TECH","BCA","M.TECH","MCA"])

# Selection Box
frameworks=st.selectbox("Choose FrameWorks :",["--options--","Scikit-Learn","Spring","React","Node.js"])

# Sliders
marks= st.slider("Enter Your Marks : ",0,100,60)
st.write(f"Your marks is = {marks}")

# taking number input 
st.number_input("How old are you ?" , min_value=18,step=1)

# taking text input
st.text_input("Enter your name : ")

# taking date time input
st.datetime_input("Enter current time and date : ")

# taking colour as input 
st.color_picker("Enter your favourite colour : ")

#taking camera input 
st.camera_input("Upload your live image : ")

# it is used for chating 
st.chat_input("Enter your chat : ")

# Taking audio as input  
st.audio_input("Enter your audio : ")





