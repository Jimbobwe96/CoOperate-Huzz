import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.title('Edit Profile')

st.write('\n\n')
student_id = st.session_state['student_id']
try:
    student_response = requests.get(f'http://api:4000/s/students/{student_id}')
    
    # 200 means the request was successful
    if student_response.status_code == 200:
        # pull the data from the response object as json
        cur_student_data = student_response.json()
    else:
        # means we got back some HTTP code besides 200
        st.error("Failed to fetch student info")
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to categories API: {str(e)}")

if cur_student_data:
    for value in cur_student_data:
        def_gpa = value.get('GPA')
        def_major = value.get('Major')
        def_cur_year = value.get('CurrentYear')
        def_home_college = value.get('HomeCollege')

# Create a Streamlit form widget
with st.form("edit_profile_form"):

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    gpa = st.number_input("Current GPA", min_value=2.00, max_value=4.00, value=def_gpa)
    major = st.text_input("Major", value=def_major)
    cur_year = st.number_input("Current Year", min_value=1, value=def_cur_year)
    home_college = st.text_input("Home College", value=def_home_college)
    # Notice here, we are using a selectbox widget.  The options for the 
    # select are provided with the 'options' parameter.
    # product_category = st.selectbox("Product Category", options=category_options, index=0)
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Edit Profile")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if gpa <= 0 or cur_year <= 0:
            st.error("Can't have 0 for GPA or Current Year")
        elif (not major or not home_college):
            st.error("Can't have an empty value for major or home college")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            student_data = {
                "gpa": gpa,
                "major": major,
                "cur_year": cur_year,
                "home_college": home_college
            }

            

            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Profile form submitted with data: {student_data}")
            
            # Now, we try to make a POST request to the proper end point
            try:
                response = requests.put(f'http://api:4000/s/students/{student_id}', json=student_data)
                if response.status_code == 200:
                    st.success("Profile edited successfully!")
                    st.switch_page('pages/Student_Profile.py')
                else:
                    st.error(f"Error editing profile: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    if back_button:
        st.switch_page("pages/Student_Profile.py")
