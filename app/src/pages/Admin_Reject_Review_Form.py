import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.title('Reject Review')

st.write('\n\n')

# Create a Streamlit form widget
with st.form("reject_review_form"):

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    details = st.text_input("Reason for Rejection")
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Reject Review")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if not details:
            st.error("Please enter a reason for rejecting")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            reject_data = {
                "details": details
            }
            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Rejection submitted with reason: {reject_data}")
            
            admin_id = st.session_state['admin_id']
            review_id = st.session_state['store_review_id']

            # Now, we try to make a POST request to the proper end point
            try:
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response1 = requests.put(f'http://api:4000/a/admins/{str(admin_id)}/reviews/{str(review_id)}/reject')
                response2 = requests.post(f'http://api:4000/a/admins/{str(admin_id)}/reviews/{str(review_id)}/reject', json=reject_data)
                del st.session_state['store_review_id']
                if response1.status_code == 200 and response2.status_code == 200:
                    st.success("Review rejected!")
                    st.switch_page('pages/Admin_Flag_Review.py')
                else:
                    st.error(f"Error rejecting review: {response1.text}")
                    st.error(f"Error rejecting review: {response2.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
                del st.session_state['store_review_id']
    if back_button:
        st.switch_page("pages/Admin_Flag_Review.py")
