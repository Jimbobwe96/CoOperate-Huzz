import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="My Reviews", layout="wide")

# Header
# Create a two-column layout with the button on the far right
col1, col2, col3 = st.columns([9, 1, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# My Reviews")
with col2:
    if st.button('Add Review', 
                type='secondary', 
                use_container_width=False):
        logger.info("Button maybe works")
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'student'
        st.switch_page('pages/Add_Student_Review.py')
with col3:
    if st.button('Back', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Student_All_Reviews.py')

# Fetch data from the API or use dummy data if the request fails
try:
    data = requests.get('http://api:4000/r/reviews').json()
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

# Display reviews from the data fetched
if isinstance(data, list): 
    for review in data:
        review_id = review.get('ReviewID', 'N/A')
        date = review.get('Date', 'N/A')
        culture = review.get('Culture', 'N/A')
        satisfaction = review.get('Satisfaction', 'N/A')
        compensation = review.get('Compensation', 'N/A')
        learning_opportunity = review.get('LearningOpportunity', 'N/A')
        work_life_balance = review.get('WorkLifeBalance', 'N/A')
        summary = review.get('Summary', 'N/A')
        position_id = review.get('PositionID', 'N/A')

        # Display the review content
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 15px;
                margin: 10px auto; 
                background-color: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            ">
                <div style="position: absolute; top: 10px; right: 15px; font-size: 14px; color: #555;">
                    <strong>{date}</strong>
                </div>
                <h4 style="margin: 0; font-size: 20px;">Review ID: {review_id}</h4>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Culture:</strong> {culture}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Satisfaction:</strong> {satisfaction}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Compensation:</strong> {compensation}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Learning Opportunity:</strong> {learning_opportunity}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Work-Life Balance:</strong> {work_life_balance}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Summary:</strong> {summary}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Position ID:</strong> {position_id}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add action buttons below the review
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"Edit Review {review_id}"):
                try:
                    response = requests.delete('http://api:4000/r/reviews/<reviewID>')
                    if response.status_code == 200:
                        st.success("Review deleted successfully!")
                    else:
                        st.error(f"Error deleting review: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to server: {str(e)}")
                    
                st.write(f"Edit Review {review_id} clicked.")
        with col2:
            if st.button(f"Delete Review {review_id}"):
                try:
                    logger.info({review_id})
                    response = requests.delete(f'http://api:4000/r/reviews/{review_id}')
                    if response.status_code == 200:
                        st.success("Review deleted successfully!")
                        st.rerun()
                    else:
                        st.error(f"Error deleting review: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to server: {str(e)}")
                st.write(f"Delete Review {review_id} clicked.")

