import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard - Flagged Reviews", layout="wide")

col1, col2 = st.columns([25, 2]) 
with col1:
    st.title("Review Flagged Reviews")
with col2:
    if st.button('Home', type='secondary', use_container_width=False):
        st.switch_page('pages/Admin_Home.py')

admin_id = st.session_state['admin_id']

try:
    data = requests.get('http://api:4000/r/reviews/flagged').json()
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
        approve_button = st.button("Approve Review: " + str(review_id))
        reject_button = st.button("Reject Review: " + str(review_id))

        if approve_button:
            try:
                response = requests.put(f'http://api:4000/r/reviews/{str(review_id)}/admin/{str(admin_id)}/approve')
                if response.status_code == 200:
                    st.success("Review approved!")
                    st.rerun()
                else:
                    st.error(f"Error approving review: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
        if reject_button:
            st.session_state['store_review_id'] = review_id
            logger.info(st.session_state['store_review_id'])
            st.switch_page("pages/Admin_Reject_Review_Form.py")

