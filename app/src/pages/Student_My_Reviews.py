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
    response = requests.get('http://api:4000/r/reviews')
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

# Filter reviews for Student_ID = 1
filtered_data = [review for review in data if review.get("StudentID") == 1]

# Display the filtered review
if filtered_data:
    # Assuming there's only one review for Student_ID = 1
    review = filtered_data[0]
    review_id = review.get('ReviewID', 'N/A')
    company = review.get('Company', 'N/A')
    title = review.get('Title', 'N/A')
    culture = review.get('Culture', 'N/A')
    satisfaction = review.get('Satisfaction', 'N/A')
    compensation = review.get('Compensation', 'N/A')
    learning_opportunity = review.get('LearningOpportunity', 'N/A')
    work_life_balance = review.get('WorkLifeBalance', 'N/A')
    summary = review.get('Summary', 'N/A')
    date = review.get('Date', 'N/A')

    # Display the review content in a box with the date on the top right
    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; padding: 16px; border-radius: 8px; position: relative;">
            <div style="position: absolute; top: 8px; right: 16px; color: #666; font-size: 14px;">{date}</div>
            <h2 style="margin: 0;">{company}</h2>
            <h3 style="margin: 0; color: #555;">{title}</h3>
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
else:
    st.write("No reviews found for Student_ID = 1.")

st.write('   ')
# Add action buttons below the review
col1, col2 = st.columns([1, 1])
with col1:
    if st.button(f"Edit Review"):
        st.session_state['passed_review_id'] = review_id
        st.switch_page("pages/Edit_Review_Form.py")
with col2:
    if st.button(f"Delete Review"):
        try:
            logger.info({review_id})
            response = requests.delete(f'http://api:4000/r/reviews/{student_id}/{position_id}')
            if response.status_code == 200:
                st.success("Review deleted successfully!")
                st.rerun()
            else:
                st.error(f"Error deleting review: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
        st.write(f"Delete Review {review_id} clicked.")
