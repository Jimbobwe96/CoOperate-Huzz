import streamlit as st
import requests

# Set page title
st.markdown("<h2>Job Postings</h2>", unsafe_allow_html=True)

# Get company ID from session state
# company_id = st.session_state['company_id']
st.session_state['company_id'] = 1
# Fetch job postings data
try:
    company_id = st.session_state['company_id']
    response = requests.get(f'http://api:4000/cr/coop_role/company/{company_id}')
    if response.status_code == 200:
        data = response.json()
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {
            "Company": "Sample Company",
            "Role": "Johnson",
            "Location": "Boston",
            "Pay": 999,
            "RequiredGPA": 3.0
        }
    ]

# Display job postings
if data:
    for item in data:
        # Extract job posting details
        company = item.get('Company', 'N/A')
        role = item.get('Role', 'N/A')
        location = item.get('Location', 'N/A')
        pay = item.get('Pay', 'N/A')
        required_gpa = item.get('Required GPA', 'N/A')
        position_id = item.get('PositionID', 'N/A')

        # Display job posting card
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 15px;
                margin: 10px auto; 
                background-color: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            ">
                <h4 style="margin: 0; font-size: 20px;">{company}</h4>
                <p style="font-size: 16px; margin: 10px 0 0 0;">{role}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Location:</strong> {location}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Pay:</strong> {pay}</p>
                <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Minimum GPA:</strong> {required_gpa}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Add view reviews button
        if st.button(f"View Reviews for {position_id}", key=f"view_reviews_{role}"):
            st.session_state['passed_position_id'] = position_id
            st.switch_page('pages/Job_Posting.py')
else:
    st.write("No data available to display.")

# Add spacing at the bottom
st.write("   ")