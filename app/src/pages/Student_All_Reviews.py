import streamlit as st

# Page configuration
st.set_page_config(page_title="All Reviews", layout="wide")

# Header
st.markdown("# All Reviews")

data = {} 

try:
    data = requests.get('http://api:4000/r/reviews').json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

