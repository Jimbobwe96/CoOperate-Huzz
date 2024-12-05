import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="Activity Log", layout="wide")

# Header
# Create a two-column layout with the button on the far right
col1, col3 = st.columns([9, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# Activity Log")
with col3:
    if st.button('Back', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Admin_Home.py')

# Fetch data from the API or use dummy data if the request fails
try:
    data = requests.get('http://api:4000/a/admins/logs').json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = [
        {"ReviewID": "123", "Date": "2024-01-01", "Culture": "Positive", "Satisfaction": "High",
         "Compensation": "Fair", "LearningOpportunity": "Good", "WorkLifeBalance": "Excellent",
         "Summary": "Great experience", "PositionID": "P123"},
        {"ReviewID": "456", "Date": "2024-02-01", "Culture": "Negative", "Satisfaction": "Low",
         "Compensation": "Poor", "LearningOpportunity": "Limited", "WorkLifeBalance": "Bad",
         "Summary": "Challenging experience", "PositionID": "P456"}
    ]

st.dataframe(data)
                    

