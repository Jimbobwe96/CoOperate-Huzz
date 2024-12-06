import streamlit as st
import requests

st.session_state['company_id'] = 1

# Configure the Streamlit page
st.set_page_config(
    page_title="Company Dashboard",
    page_icon="🏢",
    layout="wide"
)

col1, col2 = st.columns([10, 2])
with col2:
    if st.button('Sign Out', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('Home.py')

# Apply custom CSS for styling with the animated theme and positioning
st.markdown("""
    <style>
    /* Full-page gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Title styling */
    .title {
        font-size: 3rem;
        color: #ffffff;
        text-align: center;
        margin: 20px 0;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    /* Subtitle styling */
    .subtitle {
        font-size: 1.5rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
        font-family: 'Roboto', sans-serif;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }

    </style>
""", unsafe_allow_html=True)

# Header with animation overlay
st.markdown("""
    <div class="title">Company Dashboard</div>
    <div class="subtitle">Manage your company profile and job postings seamlessly</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Left Column: Company Profile
with col1:
    st.markdown("<h2>Company Profile</h2>", unsafe_allow_html=True)

    company_id = st.session_state['company_id']
    try:
        response = requests.get(f'http://api:4000/c/company/{company_id}')
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns a JSON list of reviews
        else:
            st.error(f"Error fetching data from API: {response.status_code}")
            data = []
    except Exception as e:
        st.write("**Important**: Could not connect to sample API, so using dummy data.")
        data = [
            {"Name": "Sample Company", "Industry": "Johnson", "Headquarters": "Boston"},
        ]

    # Loop through the list and display each review
    if data:  # Check if data is not empty
        for item in data:
            name = item.get('Name', 'N/A')
            industry = item.get('Industry', 'N/A')
            headquarters = item.get('Headquarters', 'N/A')

            # Display the review content
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
                    <h4 style="margin: 0; font-size: 20px;">{name}</h4>
                    <p style="font-size: 16px; margin: 10px 0 0 0;">{industry}</p>
                    <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Located In:</strong> {headquarters}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("No data available to display.")

    if st.button("Edit Profile"):
        st.write("Edit profile functionality coming soon!")
    if st.button("Delete Profile"):
        st.write("Delete profile functionality coming soon!")

# Right Column: Job Postings
with col2:
    st.markdown("<h2>Job Postings</h2>", unsafe_allow_html=True)
    company_id = st.session_state['company_id']
    try:
        response = requests.get(f'http://api:4000/cr/coop_role/company/{company_id}')
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns a JSON list of reviews
        else:
            st.error(f"Error fetching data from API: {response.status_code}")
            data = []
    except Exception as e:
        st.write("**Important**: Could not connect to sample API, so using dummy data.")
        data = [
            {"Company": "Sample Company", "Role": "Johnson", "Location": "Boston", "Pay": 999, "RequiredGPA": 3.0},
        ]

    # Loop through the list and display each review
    if data:  # Check if data is not empty
        for item in data:
            company = item.get('Company', 'N/A')
            role = item.get('Role', 'N/A')
            location = item.get('Location', 'N/A')
            pay = item.get('Pay', 'N/A')
            required_gpa = item.get('Required GPA', 'N/A')
            position_id = item.get('PositionID', 'N/A')

            # Display the review content
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
            if st.button(f"View Reviews for {role}", key=f"view_reviews_{role}"):
                st.session_state['passed_position_id'] = position_id
                st.switch_page('pages/Job_Posting.py')        
    else:
        st.write("No data available to display.")

    st.write("   ")

    if st.button('Add Co-op', 
                type='secondary', 
                use_container_width=False):
        st.session_state['authenticated'] = True
        st.switch_page('pages/Add_Job.py')
