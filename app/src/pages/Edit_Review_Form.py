import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.title('Edit Review')

st.write('\n\n')
review_id = st.session_state['passed_review_id']

try:
    review_response = requests.get(f'http://api:4000/r/reviews/{review_id}')
    
    # 200 means the request was successful
    if review_response.status_code == 200:
        # pull the data from the response object as json
        cur_review_data = review_response.json()
    else:
        # means we got back some HTTP code besides 200
        st.error("Failed to fetch review info")
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to categories API: {str(e)}")

if cur_review_data:
    for value in cur_review_data:
        def_culture = value.get('Culture')
        def_satisfaction = value.get('Satisfaction')
        def_compensation = value.get('Compensation')
        def_learning_oppurtunity = value.get('LearningOpportunity')
        def_work_life_balance = value.get('WorkLifeBalance')
        def_summary = value.get('Summary')

# Create a Streamlit form widget
with st.form("edit_review_form"):

    # try:
    #     review = requests.get(f'http://api:4000/r/reviews/{review_id}')
    #     if review.status_code == 200:
    #                     st.success("Review info pulled successfully!")
    #     else:
    #         st.error(f"Error editing review: {review.text}")
    # except requests.exceptions.RequestException as e:
    #     st.error(f"Error connecting to server: {str(e)}")

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    culture = st.number_input("Culture", min_value=1, value=def_culture)
    satisfaction = st.number_input("Satisfaction", min_value=1, max_value=5, value=def_satisfaction)
    compensation = st.number_input("Compensation", min_value=1, max_value=5, value=def_compensation)
    learning_oppurtunity = st.number_input("Learning Oppurtunity", min_value=1, max_value=5, value=def_learning_oppurtunity)
    work_life_balance = st.number_input("Work/Life Balance", min_value=1, max_value=5, value=def_work_life_balance)
    summary = st.text_input("Summary of Experience", value=def_summary)
    # Notice here, we are using a selectbox widget.  The options for the 
    # select are provided with the 'options' parameter.
    # product_category = st.selectbox("Product Category", options=category_options, index=0)
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Edit Review")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if culture <= 0 or satisfaction <= 0 or satisfaction <= 0 or compensation <= 0 or learning_oppurtunity <= 0 or work_life_balance <= 0:
            st.error("Please enter a valid rating from 1-5")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            review_data = {
                "culture": culture,
                "satisfaction": satisfaction,
                "compensation": compensation,
                "learning_oppurtunity": learning_oppurtunity,
                "work_life_balance": work_life_balance,
                "summary": summary
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
                response = requests.put(f'http://api:4000/r/reviews/{review_id}', json=review_data)
                if response.status_code == 200:
                    st.success("Review edited successfully!")
                    st.switch_page('pages/Student_My_Reviews.py')
                else:
                    st.error(f"Error editing review: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    if back_button:
        st.switch_page("pages/Student_My_Reviews.py")
