import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Internship Advisor - Home", page_icon="🌐", layout="wide")

# Page title
st.title("Co-op Advisor Portal")
st.write("Welcome to the Co-op Advisor! Navigate through the options below to assist students with their Co-op-related needs.")

# Navigation buttons
if st.button("Go to Answer Student Questions"):
    st.switch_page("pages/Advisor_FAQ.py") 

if st.button("Go to Student Compatibility Assessment"):
    st.switch_page("pages/Advisor_Comp.py") 

if st.button("Sign Out"):
    st.switch_page("Home.py") 
