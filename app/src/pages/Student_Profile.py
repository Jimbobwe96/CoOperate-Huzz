import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Student Profile", layout="wide")

# Header
# Create a two-column layout with buttons on the right
col1, col2, col3 = st.columns([9, 1, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# Student Profile")
with col2:
    if st.button('Edit Profile', type='secondary', use_container_width=False):
        logger.info("Edit Profile button clicked.")
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'student'
        st.switch_page('pages/Edit_Profile.py')
with col3:
    if st.button('Back', type='secondary', use_container_width=False):
        st.switch_page('pages/Home.py')

# Fetch data from the API
student_id = 1  # Replace with dynamic ID logic
try:
    profile = requests.get(f'http://api:4000/s/students/{student_id}').json()
except:
    st.error("Could not connect to the API. Using dummy data for demonstration.")
    profile = {
        "FirstName": "John",
        "LastName": "Doe",
        "GPA": 3.8,
        "Major": "Computer Science",
        "CurrentYear": 3,
        "HomeCollege": "Engineering College",
        "skills": [{"SkillName": "Python", "Proficiency": 9}],
        "experiences": [{"Title": "Intern", "Company": "TechCorp", "StartTime": "2022-05-01", "EndTime": "2022-08-31"}]
    }

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
        <h2 style="margin-bottom: 5px;">{profile['FirstName']} {profile['LastName']}</h2>
        <p style="margin: 0;"><strong>Major:</strong> {profile['Major']}</p>
        <p style="margin: 0;"><strong>Current Year:</strong> Year {profile['CurrentYear']}</p>
        <p style="margin: 0;"><strong>GPA:</strong> {profile['GPA']}</p>
        <p style="margin: 0;"><strong>Home College:</strong> {profile['HomeCollege']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Display skills
st.markdown("## Skills")
for skill in profile['skills']:
    st.markdown(
        f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin: 5px auto;
            background-color: #fff;
        ">
            <p style="margin: 0;"><strong>{skill['SkillName']}</strong> (Proficiency: {skill['Proficiency']})</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Display experiences
st.markdown("## Experiences")
for exp in profile['experiences']:
    st.markdown(
        f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin: 5px auto;
            background-color: #fff;
        ">
            <h4 style="margin-bottom: 5px;">{exp['Title']} at {exp['Company']}</h4>
            <p style="margin: 0;"><strong>Start:</strong> {exp['StartTime']} | <strong>End:</strong> {exp['EndTime']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Add action buttons for experiences
st.markdown("## Actions")
for i, exp in enumerate(profile['experiences']):
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button(f"Edit Experience {i+1}"):
            st.write(f"Edit Experience {i+1} clicked.")  # Replace with logic to edit experience
    with col2:
        if st.button(f"Delete Experience {i+1}"):
            st.write(f"Delete Experience {i+1} clicked.")  # Replace with logic to delete experience
