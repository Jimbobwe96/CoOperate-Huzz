import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.session_state['advisor_id'] = 1
# Page configuration
st.set_page_config(page_title="My Students", layout="wide")
advisor_id = st.session_state['advisor_id']

# Header
# Create a two-column layout with the button on the far right
col1, col2, col3 = st.columns([9, 1, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# My Students")
with col2:
    if st.button('Add Student', 
                type='secondary', 
                use_container_width=False):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'advisor'
        st.switch_page('pages/Advisor_Add_Student_Form.py')
with col3:
    if st.button('Back', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Advisor_Home.py')

# Fetch data from the API or use dummy data if the request fails
try:
    response = requests.get(f'http://api:4000/s/students/advisor/{advisor_id}')
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
# Display the filtered review
if data:
    for student in data:
        student_id = student.get('StudentID')
        full_name = student.get('FirstName') + " " + student.get('LastName')
        email = student.get('Email')
        gpa = student.get('GPA')
        major = student.get('Major')
        cur_year = student.get('CurrentYear')
        college = student.get('HomeCollege')

        # Display the review content
        st.markdown(
                f"""
                <div class="review-card">
                    <div class="review-header">
                        <h2>Student Info</h2>
                    </div>
                    <div class="student_info">
                        <p><strong>Name: </strong> {student.get('FirstName') + " " + student.get('LastName')}</p>
                        <p><strong>Major: </strong> {student.get('Major')}</p>
                        <p><strong>Home College:</strong> {student.get('HomeCollege')}</p>
                        <p><strong>GPA:</strong> {student.get('GPA')}</p>
                        <p><strong>Current Year:</strong> {student.get('CurrentYear')}</p>
                        <p><strong>Email:</strong> {student.get('Email')}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        
        if st.button(f"Remove Student: {student_id}"):
            try:
                response = requests.put(f'http://api:4000/s/students/{student["StudentID"]}/advisor/remove')
                if response.status_code == 200:
                    st.success("Student removed successfully!")
                    st.rerun()
                else:
                    st.error(f"Error removing student: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
else:
    st.write("No students found for this advisor")
        # Add action buttons below the review


