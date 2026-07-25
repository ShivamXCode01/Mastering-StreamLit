import streamlit as st

# it is used to give heading 
st.title("Namsate Duniya!")

# it is used to give sub Header /Sub title 
st.subheader("Learn & Grow")

# it is used to give paragraph
st.text("This is my first app using StreamLit ")

st.write("Hello BhaiLog chalo Start Karte hai ")

#Select Box  :- using this we can select multiple things according to our desirea
Interest=st.selectbox("Your Favourite subject : ",["DSA","MERN","AI","ML"])

st.write(f"You choosed {Interest} Excellent Choice")

# We can also print success message 
st.success(f"Well Done you selected {Interest}")

# Using this we can also integrate html in the StreaLi

html_temp = """
    <div>
    <h2>Welcome</h2>
    </div>
"""

st.markdown(html_temp,unsafe_allow_html=True)

