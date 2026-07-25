import requests
import streamlit as st

st.set_page_config(page_title="Global Currency Converter", page_icon="💱")
st.title("💱 Advanced Currency Exchanger")
st.subheader("Dynamic Multi-Currency Selection via API")


# Function to fetch all available currencies dynamically
@st.cache_data
def get_currencies():
  url = "https://api.frankfurter.app/currencies"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()  # Returns dict like {"USD": "United States Dollar", "INR": "Indian Rupee", ...}
  return {"USD": "United States Dollar", "EUR": "Euro"}  # Fallback


currencies = get_currencies()
# Create a clean list for selectboxes (e.g., "USD - United States Dollar")
currency_options = [f"{code} - {name}" for code, name in currencies.items()]

# Layout using columns for a cleaner interface
col1, col2 = st.columns(2)

with col1:
  from_selection = st.selectbox(
      "From Currency:", currency_options, index=currency_options.index("INR - Indian Rupee") if "INR - Indian Rupee" in currency_options else 0
  )

with col2:
  to_selection = st.selectbox(
      "To Currency:", currency_options, index=currency_options.index("USD - United States Dollar") if "USD - United States Dollar" in currency_options else 1
  )

# We Extracting  just the 3-letter currency code 
from_currency = from_selection.split(" ")[0]
to_currency = to_selection.split(" ")[0]

# Amount input from user 
amount = st.number_input(
    f"Enter amount in {from_currency}:", min_value=0.0, value=1.0, step=1.0
)

if st.button("Convert Currency", type="primary"):
  if from_currency == to_currency:
    st.warning("Please select two different currencies to convert.")
  else:
    # API call with dynamic 'from' and 'to' parameters
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      converted_amount = data["rates"][to_currency]

      # Display output clearly
      st.success(
          f"### {amount:,.2f} {from_currency} = {converted_amount:,.2f}"
          f" {to_currency}"
      )

      # Display metadata / exchange rate info
      exchange_rate = data["rates"][to_currency] / amount
      st.caption(
          f"Exchange Rate: 1 {from_currency} = {exchange_rate:.4f}"
          f" {to_currency}"
      )
    else:
      st.error(
          "Failed to fetch exchange rates. The currency pair might not be"
          " supported currently."
      )