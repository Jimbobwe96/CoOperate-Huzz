import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Student Profile", layout="wide")

# Header
# Create a two-column layout with buttons on the right
col1, col2 = st.columns([10, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# Student Profile")
with col2:
    if st.button('Back', type='secondary', use_container_width=False):
        st.switch_page('pages/Student_Home.py')

# Fetch data from the API
student_id = 1 
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
        with st.form("edit_profile_form"):
            st.text_input("First Name", first_name, key="edit_first_name")
            st.text_input("Last Name", last_name, key="edit_last_name")
            st.text_input("Major", major, key="edit_major")
            st.number_input("GPA", value=gpa, min_value=0.0, max_value=4.0, step=0.1, key="edit_gpa")
            st.number_input("Current Year", value=current_year, min_value=1, max_value=4, step=1, key="edit_current_year")
            st.text_input("Home College", home_college, key="edit_home_college")
            
            # Submit button for the form
            submitted = st.form_submit_button("Save Changes")

        if submitted:
            # Collect updated data
            updated_data = {
                "FirstName": st.session_state["edit_first_name"],
                "LastName": st.session_state["edit_last_name"],
                "Major": st.session_state["edit_major"],
                "GPA": st.session_state["edit_gpa"],
                "CurrentYear": st.session_state["edit_current_year"],
                "HomeCollege": st.session_state["edit_home_college"]
            }

            try:
                # Make PUT request to update the profile
                response = requests.put(f'http://api:4000/s/students/{student_id}', json=updated_data)
                if response.status_code == 200:
                    st.success("Profile updated successfully!")
                    
                    # Refresh the updated profile data
                    updated_profile = requests.get(f'http://api:4000/s/students/{student_id}').json()
                    
                    # Update local variables with new profile data
                    first_name = updated_profile.get("FirstName", "N/A")
                    last_name = updated_profile.get("LastName", "N/A")
                    major = updated_profile.get("Major", "N/A")
                    gpa = updated_profile.get("GPA", "N/A")
                    current_year = updated_profile.get("CurrentYear", "N/A")
                    home_college = updated_profile.get("HomeCollege", "N/A")
                else:
                    st.error(f"Error updating profile: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")

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







