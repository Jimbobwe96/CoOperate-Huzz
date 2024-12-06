import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests

st.set_page_config(layout='wide')

st.title('Edit Company Profile')

st.write('\n\n')
company_id = st.session_state['company_id']

# Fetch current company data
try:
    company_response = requests.get(f'http://api:4000/c/company/{company_id}')
    if company_response.status_code == 200:
        cur_company_data = company_response.json()
    else:
        st.error("Failed to fetch company info")
        cur_company_data = None
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to API: {str(e)}")
    cur_company_data = None

# Set default values from current data
if cur_company_data:
    for value in cur_company_data:
        def_name = value.get('Name', '')
        def_headquarters = value.get('Headquarters', '')
        def_industry = value.get('Industry', '')
        def_size = value.get('Size', 'S')

# Create size options with friendly labels
size_options = {
    'S': 'Small (< 100 employees)',
    'M': 'Medium (100-1000 employees)',
    'L': 'Large (1000+ employees)'
}

# Create a Streamlit form widget
with st.form("edit_profile_form"):
    name = st.text_input("Company Name", value=def_name, max_chars=50)
    headquarters = st.text_input("Headquarters", value=def_headquarters)
    industry = st.text_input("Industry", value=def_industry)
    
    # Create a radio button for size selection with friendly labels
    size = st.radio(
        "Company Size",
        options=list(size_options.keys()),
        format_func=lambda x: size_options[x],
        index=list(size_options.keys()).index(def_size)
    )
    
    # Add the submit and cancel buttons
    col1, col2 = st.columns([1, 5])
    with col1:
        submit_button = st.form_submit_button("Save Changes")
    with col2:
        back_button = st.form_submit_button("Cancel")
    
    # Handle form submission
    if submit_button:
        # Validate all fields are filled
        if not all([name, headquarters, industry, size]):
            st.error("All fields are required")
        else:
            # Package the data
            company_data = {
                "name": name,
                "headquarters": headquarters,
                "industry": industry,
                "size": size
            }
            
            logger.info(f"Profile form submitted with data: {company_data}")
            
            # Make PUT request to update company data
            try:
                response = requests.put(f'http://api:4000/c/company/{company_id}', json=company_data)
                if response.status_code == 200:
                    st.success("Company profile updated successfully!")
                    st.switch_page('pages/Company_Profile.py')
                else:
                    st.error(f"Error updating profile: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
    
    if back_button:
        st.switch_page("pages/Company_Profile.py")