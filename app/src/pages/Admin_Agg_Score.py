import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard - Aggregated Scores", layout="wide")

st.title("Aggregated Scores for Companies")
st.write("Select a company to view its aggregated score.")

# Example list of company links (can be generated dynamically)
companies = ["Company A", "Company B", "Company C", "Company D"]
for company in companies:
    st.markdown(f"- [View scores for {company}](#)")

# Navigation buttons
if st.button("Home"):
    st.switch_page("pages/Admin_Home.py")
