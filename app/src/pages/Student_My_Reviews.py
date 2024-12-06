import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="My Reviews", layout="wide")
st.session_state['student_id'] = 1

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
    student_id = st.session_state['student_id']
    response = requests.get(f'http://api:4000/r/reviews/student/{str(student_id)}')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.warning("**Important**: Could not connect to the sample API, so using dummy data.")
    data = [
        {
            "Company": "John Inc",
            "Title": "John",
            "Culture": 2,
            "Satisfaction": 2,
            "Compensation": 2,
            "LearningOpportunity": 2,
            "WorkLifeBalance": 2,
            "Summary": "Great experience",
            "Date": "2024-12-05"
        },
        {
            "Company": "Samuel Inc",
            "Title": "Sam",
            "Culture": 2,
            "Satisfaction": 5,
            "Compensation": 5,
            "LearningOpportunity": 5,
            "WorkLifeBalance": 5,
            "Summary": "Good learning curve",
            "Date": "2024-11-25"
        }
    ]

if data:
    for review in data:
        company = review.get('Company')
        position_id = review.get('PositionID')
        review_id = review.get('ReviewID')
        role = review.get('Role')
        culture = review.get('Culture')
        satisfaction = review.get('Satisfaction')
        compensation = review.get('Compensation')
        learning_opportunity = review.get('LearningOpportunity')
        work_life_balance = review.get('WorkLifeBalance')
        summary = review.get('Summary')
        date = review.get('Date')

        # Display the review content in a box with the date on the top right
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; padding: 16px; border-radius: 8px; position: relative;">
                <div style="position: absolute; top: 8px; right: 16px; color: #666; font-size: 14px;">{date}</div>
                <h2 style="margin: 0;">{company}</h2>
                <h3 style="margin: 0; color: #555;">{role}</h3>
                <div style="margin-top: 16px;">
                    <p><strong>Culture:</strong> {culture}</p>
                    <p><strong>Satisfaction:</strong> {satisfaction}</p>
                    <p><strong>Compensation:</strong> {compensation}</p>
                    <p><strong>Learning Opportunity:</strong> {learning_opportunity}</p>
                    <p><strong>Work-Life Balance:</strong> {work_life_balance}</p>
                    <p><strong>Summary:</strong> {summary}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write('   ')
        # Add action buttons below the review
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"Edit Review: {review_id}"):
                st.session_state['passed_review_id'] = review_id
                st.switch_page("pages/Edit_Review_Form.py")
        with col2:
            if st.button(f"Delete Review: {review_id}"):
                try:
                    response = requests.delete(f'http://api:4000/r/reviews/{review_id}')
                    if response.status_code == 200:
                        st.success("Review deleted successfully!")
                        st.rerun()
                    else:
                        st.error(f"Error deleting review: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to server: {str(e)}")
                st.write(f"Delete Review {review_id} clicked.")
else:
    st.write("No reviews found for the Student")