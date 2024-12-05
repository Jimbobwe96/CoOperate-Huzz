import streamlit as st
import requests
import logging
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Activity Log", 
    page_icon="📜", 
    layout="wide"
)

# Apply custom CSS for the theme
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header styling */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        margin-bottom: 30px;
    }

    .header-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.6);
    }

    .back-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: bold;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 25px;
        text-align: center;
        text-decoration: none;
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .back-button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }

    /* Table styling */
    .custom-table {
        margin-top: 20px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
st.markdown(
    """
    <div class="header">
        <div class="header-title">Activity Log</div>
        <a href="/" class="back-button">⬅️ Back</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Fetch data from the API or use dummy data if the request fails
try:
    data = requests.get('http://api:4000/a/admins/logs').json()
except:
    st.warning("**Important**: Could not connect to the API. Using dummy data.")
    data = [
        {"ReviewID": "123", "Date": "2024-01-01", "Culture": "Positive", "Satisfaction": "High",
         "Compensation": "Fair", "LearningOpportunity": "Good", "WorkLifeBalance": "Excellent",
         "Summary": "Great experience", "PositionID": "P123"},
        {"ReviewID": "456", "Date": "2024-02-01", "Culture": "Negative", "Satisfaction": "Low",
         "Compensation": "Poor", "LearningOpportunity": "Limited", "WorkLifeBalance": "Bad",
         "Summary": "Challenging experience", "PositionID": "P456"}
    ]

# Display data in a visually appealing table
st.markdown("<div class='custom-table'>", unsafe_allow_html=True)
st.dataframe(data)
st.markdown("</div>", unsafe_allow_html=True)
