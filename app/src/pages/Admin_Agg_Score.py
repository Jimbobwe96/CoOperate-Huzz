import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard - Aggregated Scores", layout="wide")

col1, col2 = st.columns([25, 2]) 
with col1:
    st.title("Aggregated Scores for Companies")
with col2:
    if st.button('Home', type='secondary', use_container_width=False):
        st.switch_page('pages/Admin_Home.py')

# Example list of company links (can be generated dynamically)
companies = ["Company A", "Company B", "Company C", "Company D"]
for company in companies:
    st.markdown(f"- [View scores for {company}](#)")

