import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.session_state['company_id'] = 1

st.set_page_config(layout = 'wide')

st.title('Add New Co-op')

st.write('\n\n')

# Create a Streamlit form widget
with st.form("add_review_form"):

# Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    title = st.text_input("Title")
    city = st.text_input("City")
    country = st.text_input("Country")
    pay = st.number_input("Compensation", min_value=0)
    required_gpa = st.number_input("Required GPA", min_value=0.00, max_value=4.00)
    # Notice here, we are using a selectbox widget.  The options for the 
    # select are provided with the 'options' parameter.
    # product_category = st.selectbox("Product Category", options=category_options, index=0)
    
    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Add Co-op")
    back_button = st.form_submit_button("Cancel")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if not (title or city or country or pay or required_gpa):
            st.error("Please enter a value")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            job_data = {
                "title": title,
                "city": city,
                "country": country,
                "pay": pay,
                "required_gpa": required_gpa,
            }
            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Review form submitted with data: {job_data}")
            
            # Now, we try to make a POST request to the proper end point
            try:
                company_id = st.session_state['company_id']
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.post(f'http://api:4000/cr/coop_role/company/{company_id}', json=job_data)
                if response.status_code == 200:
                    st.success("Co-op added successfully!")
                    st.switch_page('pages/Company_Home.py')
                else:
                    st.error(f"Error adding job: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    if back_button:
        st.switch_page("pages/Company_Home.py")
