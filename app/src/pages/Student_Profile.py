import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Student Profile", layout="wide")
st.session_state['student_id'] = 1

# Header
# Create a two-column layout with buttons on the right
col1, col2 = st.columns([10, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# Student Profile")
with col2:
    if st.button('Back', type='secondary', use_container_width=False):
        st.switch_page('pages/Student_Home.py')

# Fetch data from the API
student_id = st.session_state['student_id']
try:
    profile = requests.get(f'http://api:4000/s/students/{str(student_id)}').json()
except:
    st.error("Could not connect to the API. Using dummy data for demonstration.")
    profile = {
        "Student_ID": 1,
        "FirstName": "John",
        "LastName": "Doe",
        "GPA": 3.8,
        "Major": "Computer Science",
        "CurrentYear": 3,
        "HomeCollege": "Engineering College",
    }

# If `profile` is a list, use the first entry; otherwise, use it as a single profile
if isinstance(profile, list):
    if len(profile) > 0:
        profile = profile[0] 
    else:
        st.error("No profiles available.")
        st.stop()

# Extract fields from the profile
first_name = profile.get('FirstName', 'N/A')
last_name = profile.get('LastName', 'N/A')
full_name = first_name + " " + last_name
gpa = profile.get('GPA', 'N/A')
major = profile.get('Major', 'N/A')
current_year = profile.get('CurrentYear', 'N/A')
home_college = profile.get('HomeCollege', 'N/A')

# Display profile information
st.markdown(
    f"""
    <div style="
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto; 
        background-color: #f9f9f9;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    ">
        <h2 style="margin-bottom: 5px;">{first_name} {last_name}</h2>
        <p style="margin: 0;"><strong>Major:</strong> {major}</p>
        <p style="margin: 0;"><strong>Current Year:</strong> Year {current_year}</p>
        <p style="margin: 0;"><strong>GPA:</strong> {gpa}</p>
        <p style="margin: 0;"><strong>Home College:</strong> {home_college}</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    if st.button('Edit Profile', type='secondary', use_container_width=True):
        # Create a form for editing profile details
        st.switch_page('pages/Edit_Student_Profile.py')
# Functionality for deleting Student. Will finish later
# with col2:
#     st.button('Delete Profile', type ='secondary', use_container_width=True)

st.markdown("   ")

# Skills Information 
try:
    skills = requests.get(f'http://api:4000/sk/skills/student/{student_id}').json()
except:
    st.error("Could not connect to the API. Using dummy data for demonstration.")
    skills = {
        "Student_ID": 1,
        "SkillID": 1,
        "Proficiency": 9,
    }

if skills:
    st.subheader("Skills")
    for item in skills:
        skill_id = item.get('SkillID')
        skill = item.get('Skill')
        proficiency = item.get('Proficiency')

        # Display profile information
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 20px;
                margin: 20px auto; 
                background-color: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            ">
                <p style="margin: 0;"><strong>Skill: </strong>{skill}</p>
                <p style="margin: 0;"><strong>Proficiency: </strong>{proficiency}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Remnants of functionality for trying to get Edit Skills, Delete Skills, and Add Skills to work
        # Will work on this more once project is over
        # col1, col2, col3 = st.columns([1, 1, 6])
        # with col1:
        #     st.button('Edit Skill', type='secondary', use_container_width=True)
        # with col2:
        #     st.button('Delete Skill', type ='secondary', use_container_width=True)

# experience 
try:
    exp = requests.get(f'http://api:4000/e/experiences/{student_id}').json()
except:
    st.error("Could not connect to the API. Using dummy data for demonstration.")
    exp = {
        "ExperienceID": 1,
        "Student_ID": 1,
        "Title": "Audit",
        "Industry": "Accounting",
        "StartTime": 2024,
        "EndTime": 2024,
        "Company": "Google",
    }

# If `profile` is a list, use the first entry; otherwise, use it as a single profile
if exp:
    st.subheader("Previous Experiences")
    for e in exp:
        # Extract fields from the profile
        experience_id = e.get('ExperienceID')
        student_id = e.get('Student_ID')
        title = e.get('Title')
        industry = e.get('Industry')
        start_time = e.get('StartTime')
        end_time = e.get('EndTime')
        company = e.get('Company')

        # Display profile information
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 20px;
                margin: 20px auto; 
                background-color: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            ">
                <p style="margin: 0;"><strong>Company:</strong> Year {company}</p>
                <p style="margin: 0;"><strong>Job Title:</strong> Year {title}</p>
                <p style="margin: 0;"><strong>Industry:</strong> {industry}</p>
                <p style="margin: 0;"><strong>Started:</strong> Year {start_time}</p>
                <p style="margin: 0;"><strong>Ended:</strong> {end_time}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Remnants of functionality for Editing, Deleting, and Adding Experiences
        # Will work more on when project is over
        # col1, col2, col3 = st.columns([1, 1, 6])

        # with col1:
        #     st.button('Edit Experience', type='secondary', use_container_width=True)

        # with col2:
        #     st.button('Delete Experience', type ='secondary', use_container_width=True)







