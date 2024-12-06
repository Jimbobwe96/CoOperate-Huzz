import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.title('Add New Review')

st.write('\n\n')

# Create a Streamlit form widget
with st.form("add_review_form"):

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    student_id = st.text_input("Student ID")
    culture = st.number_input("Culture", min_value=1, max_value=5)
    satisfaction = st.number_input("Satisfaction", min_value=1, max_value=5)
    compensation = st.number_input("Compensation", min_value=1, max_value=5)
    learning_oppurtunity = st.number_input("Learning Oppurtunity", min_value=1, max_value=5)
    work_life_balance = st.number_input("Work/Life Balance", min_value=1, max_value=5)
    summary = st.text_input("Summary of Experience")
    position_id = st.text_input("Position ID")
    # Notice here, we are using a selectbox widget.  The options for the 
    # select are provided with the 'options' parameter.
    # product_category = st.selectbox("Product Category", options=category_options, index=0)
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Add Review")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if not student_id:
            st.error("Please enter a student id")
        elif not (culture or satisfaction or satisfaction or compensation or learning_oppurtunity or work_life_balance):
            st.error("Please enter a rating")
        elif culture <= 0 or satisfaction <= 0 or satisfaction <= 0 or compensation <= 0 or learning_oppurtunity <= 0 or work_life_balance <= 0:
            st.error("Please enter a valid rating from 1-5")
        elif not position_id:
            st.error("Please enter a position id")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            review_data = {
                "student_id": student_id,
                "culture": culture,
                "satisfaction": satisfaction,
                "compensation": compensation,
                "learning_oppurtunity": learning_oppurtunity,
                "work_life_balance": work_life_balance,
                "summary": summary,
                "position_id": position_id
            }
            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Review form submitted with data: {review_data}")
            
            # Now, we try to make a POST request to the proper end point
            try:
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.post('http://api:4000/r/reviews', json=review_data)
                if response.status_code == 200:
                    st.success("Review added successfully!")
                    st.switch_page('pages/Student_My_Reviews.py')
                else:
                    st.error(f"Error adding review: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    if back_button:
        st.switch_page("pages/Student_My_Reviews.py")
