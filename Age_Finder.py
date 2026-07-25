import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Age Finder",page_icon='🕰️',layout='wide')

st.title("Age Finder")
st.write("Enter your date of birth below to find out your exact age in years, months, and days!")

dob = st.date_input("Select your Date of Birth :", value=date(2000,1,1),
                    min_value=date(1900,1,1),max_value=date.today())

Button = st.button("Calculate Age",type="primary")

if Button:
    Today_date = date.today()

    if dob > Today_date:
        st.write("Error ! We can't predict your future age...")
    else:
        age_data = relativedelta(Today_date,dob)

    total_days = (Today_date - dob).days
    total_weeks = total_days // 7
    total_months = age_data.years * 12 + age_data.months

    st.success("Calculation Successful!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Years", age_data.years)
    col2.metric("Months", age_data.months)
    col3.metric("Days", age_data.days)
    
    st.markdown("****")
    st.subheader("📊 Breakdown in Other Units")
    
        
    st.markdown(f"* **Total Months Lived:** {total_months:,} months")
    st.markdown(f"* **Total Weeks Lived:** {total_weeks:,} weeks")
    st.markdown(f"* **Total Days Lived:** {total_days:,} days")