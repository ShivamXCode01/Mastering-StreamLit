import streamlit as st

st.title("In this We Discuss about the layouts in the StreamLit")

#Columns allow you to split your horizontal space into multiple vertical containers
col1 ,col2 = st.columns(2)

# each column treated as new page
with col1:
    st.subheader("Masala Chai")
with col2:
    st.subheader("Elachi Chai")

# sidebar
st.sidebar.text_input("Enter your name : ")
st.sidebar.radio("Enter your gender :",["Male","Female"])

# Expander

with st.expander("Show My Academic details: "):
    st.write("""
        1. 10 Th :-- 82%
        2. 12 Th :-- 65%
        3. Till 2nd Year :-- 8.53 CGPA
    """)
