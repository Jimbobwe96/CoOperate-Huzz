import streamlit as st
import requests
import logging
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="My Reviews", 
    page_icon="📝", 
    layout="wide"
)

col1, col2 = st.columns([9, 1])
with col2:
    if st.button("Back"):
        st.switch_page('pages/Admin_Home.py')

# Apply custom CSS for styling
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

    .nav-button {
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

    .nav-button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }

    /* Review card styling */
    .review-card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .review-card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.5);
    }

    .review-card h4 {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ffffff;
    }

    .review-card p {
        font-size: 1rem;
        color: #ffffff;
        margin: 5px 0;
    }

    .action-button {
        font-size: 1rem;
        font-weight: bold;
        padding: 10px 20px;
        margin-top: 10px;
        border: none;
        border-radius: 25px;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .action-button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
st.markdown(
    """
    <div class="header">
        <div class="header-title">All Reviews</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Fetch data from the API or use dummy data if the request fails
try:
    data = requests.get('http://api:4000/a/admins/reviews').json()
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

# Display reviews from the data fetched
if isinstance(data, list): 
    for review in data:
        st.markdown(
            f"""
            <div class="review-card">
                <h4>Review ID: {review.get('ReviewID', 'N/A')}</h4>
                <p><strong>Date:</strong> {review.get('Date', 'N/A')}</p>
                <p><strong>Culture:</strong> {review.get('Culture', 'N/A')}</p>
                <p><strong>Satisfaction:</strong> {review.get('Satisfaction', 'N/A')}</p>
                <p><strong>Compensation:</strong> {review.get('Compensation', 'N/A')}</p>
                <p><strong>Learning Opportunity:</strong> {review.get('LearningOpportunity', 'N/A')}</p>
                <p><strong>Work-Life Balance:</strong> {review.get('WorkLifeBalance', 'N/A')}</p>
                <p><strong>Summary:</strong> {review.get('Summary', 'N/A')}</p>
                <p><strong>Position ID:</strong> {review.get('PositionID', 'N/A')}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Add a flag button for each review
        if st.button(f"🚩 Flag Review: {review['ReviewID']}", key=f"flag_{review['ReviewID']}"):
            try:
                response = requests.put(f'http://api:4000/r/reviews/{review["ReviewID"]}/flag')
                if response.status_code == 200:
                    st.success("Review flagged successfully!")
                    st.rerun()
                else:
                    st.error(f"Error flagging review: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
