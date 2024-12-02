import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard - Home", layout="wide")

st.title("Welcome to the Admin Dashboard")
st.write("Use the buttons below to navigate to different sections.")

# Navigation buttons
if st.button("Go to Aggregated Scores"):
    st.switch_page("pages/Admin_Agg_Score.py")

if st.button("Go to Flagged Reviews"):
    st.switch_page("pages/Admin_Flag_Review.py")

# Sign out button
if st.button("Sign Out"):
    st.switch_page("Home.py")
