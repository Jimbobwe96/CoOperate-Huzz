import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="All Reviews", layout="wide")

# Header
# Create a two-column layout with the button on the far right
col1, col2, col3 = st.columns([8, 1, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# All Reviews")
with col2:
    if st.button('My Reviews', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Student_My_Reviews.py')
with col3:
    if st.button('Home', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Student_Home.py')

# Fetch data from the API or use dummy data if the request fails
try:
    data = requests.get('http://api:4000/r/reviews').json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = {
        "a":{"b": "123", "c": "hello"},
        "z": {"b": "456", "c": "goodbye"}}

# Display reviews from the data fetched
if isinstance(data, list): 
    for review in data:
        review_id = review.get('ReviewID', 'N/A')
        student_id = review.get('StudentID', 'N/A')
        date = review.get('Date', 'N/A')
        culture = review.get('Culture', 'N/A')
        satisfaction = review.get('Satisfaction', 'N/A')
        compensation = review.get('Compensation', 'N/A')
        learning_opportunity = review.get('LearningOpportunity', 'N/A')
        work_life_balance = review.get('WorkLifeBalance', 'N/A')
        summary = review.get('Summary', 'N/A')
        flagged = review.get('Flagged', 'N/A')
        resolved_by = review.get('ResolvedBy', 'N/A')
        position_id = review.get('PositionID', 'N/A')

        # Display in a formatted way
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


