import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Company Profile", layout="wide")
st.session_state['company_id'] = 1

# Header
# Create a two-column layout with buttons on the right
col1, col2 = st.columns([10, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# Company Profile")
with col2:
    if st.button('Back', type='secondary', use_container_width=False):
        st.switch_page('pages/Company_Home.py')

# Fetch data from the API
company_id = st.session_state['company_id']
try:
    profile = requests.get(f'http://api:4000/c/company/{str(company_id)}').json()
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
company_name = profile.get('Name', 'N/A')
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
        <h2 style="margin-bottom: 5px;">{company_name}</h2>
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
with col2:
    st.button('Delete Profile', type ='secondary', use_container_width=True)

st.markdown("   ")

# Skills Information 
student_id = 1
try:
    skill = requests.get(f'http://api:4000/sk/skills/{student_id}').json()
except:
    st.error("Could not connect to the API. Using dummy data for demonstration.")
    skill = {
        "Student_ID": 1,
        "SkillID": 1,
        "Proficiency": 9,
    }

# If `profile` is a list, use the first entry; otherwise, use it as a single profile
if isinstance(skill, list):
    if len(skill) > 0:
        skill = skill[0] 
    else:
        st.error("No skills available.")
        st.stop()

# Extract fields from the profile
student_id = skill.get('Student_ID', 'N/A')
skill_id = skill.get('SkillID', 'N/A')
proficiency = skill.get('Proficiency', 'N/A')

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
        <h2 style="margin-bottom: 5px;">{student_id}</h2>
        <p style="margin: 0;"><strong>Skill: </strong>{skill_id}</p>
        <p style="margin: 0;"><strong>Proficiency: </strong>{proficiency}</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.button('Edit Skill', type='secondary', use_container_width=True)

with col2:
    st.button('Delete Skill', type ='secondary', use_container_width=True)

# experience 
student_id = 1
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
if isinstance(exp, list):
    if len(exp) > 0:
        exp = exp[0] 
    else:
        st.error("No skills available.")
        st.stop()

# Extract fields from the profile
experience_id = exp.get('ExperienceID', 'N/A')
student_id = exp.get('Student_ID', 'N/A')
title = exp.get('Title', 'N/A')
industry = exp.get('Industry', 'N/A')
start_time = exp.get('StartTime', 'N/A')
end_time = exp.get('EndTime', 'N/A')
company = exp.get('Company', 'N/A')

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
        <p style="margin: 0;"><strong>Experience:</strong> {experience_id}</p>
        <p style="margin: 0;"><strong>Job Title:</strong> Year {title}</p>
        <p style="margin: 0;"><strong>Industry:</strong> {industry}</p>
        <p style="margin: 0;"><strong>Started:</strong> Year {start_time}</p>
        <p style="margin: 0;"><strong>Ended:</strong> {end_time}</p>
        <p style="margin: 0;"><strong>Company:</strong> Year {company}</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.button('Edit Experience', type='secondary', use_container_width=True)

with col2:
    st.button('Delete Experience', type ='secondary', use_container_width=True)

