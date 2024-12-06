import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.title('Add Student')

st.write('\n\n')

# Create a Streamlit form widget
with st.form("add_student_form"):

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    student_id = st.text_input("StudentID")
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Add Student")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if not student_id:
            st.error("Please enter a student id")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            advisor_student_data = {
                "student_id": student_id
            }
            
            advisor_id = st.session_state['advisor_id']

            # Now, we try to make a POST request to the proper end point
            try:
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.put(f'http://api:4000/s/students/advisor/{str(advisor_id)}/add', json=advisor_student_data)
                if response.status_code == 200:
                    st.success("Student Added!")
                    st.switch_page('pages/Advisor_Students.py')
                else:
                    st.error(f"Error adding student: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    if back_button:
        st.switch_page("pages/Advisor_Students.py")
