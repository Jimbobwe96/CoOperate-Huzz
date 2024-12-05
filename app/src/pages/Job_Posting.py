import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="My Postings Reviews", layout="wide")

# Header
# Create a two-column layout with the button on the far right
col1, col2, col3 = st.columns([9, 1, 1])  # Adjust proportions as needed
with col1:
    st.markdown("# My Postings Reviews")
with col3:
    if st.button('Back', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Company_Home.py')

position_id = st.session_state['company_id']
try:
    response = requests.get(f'http://api:4000/cr/cooprole/{position_id}')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {"CompanyID": 1, "Title": "Johnson", "City": "Boston", "Country": "US",
         "Pay": 1456, "RequiredGPA": 3.0},

    ]
# Filter reviews for Student_ID = 1
filtered_data = [role for role in data if role.get("CompanyID") == 1]

# Display the filtered review
if filtered_data:
    # Assuming there's only one review for Student_ID = 1
    role = filtered_data[0]
    company_id = role.get('CompanyID', 'N/A')
    title = role.get('Title', 'N/A')
    city = role.get('City', 'N/A')
    country = role.get('Country', 'N/A')
    pay = role.get('Pay', 'N/A')
    required_gpa = role.get('RequiredGPA', 'N/A')

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
            <h4 style="margin: 0; font-size: 20px;">Company ID: {company_id}</h4>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Role:</strong> {title}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Location:</strong> {city}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Pay:</strong> {pay}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Minimum GPA:</strong> {required_gpa}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("No reviews found for PositionID = 1.")



# Fetch data from the API or use dummy data if the request fails
try:
    response = requests.get('http://api:4000/r/reviews')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {"ReviewID": "123", "Date": "2024-01-01", "Culture": "Positive", "Satisfaction": "High",
         "Compensation": "Fair", "LearningOpportunity": "Good", "WorkLifeBalance": "Excellent",
         "Summary": "Great experience", "PositionID": "P123", "Student_ID": 1},
        {"ReviewID": "456", "Date": "2024-02-01", "Culture": "Negative", "Satisfaction": "Low",
         "Compensation": "Poor", "LearningOpportunity": "Limited", "WorkLifeBalance": "Bad",
         "Summary": "Challenging experience", "PositionID": "P456", "Student_ID": 2}
    ]
# Filter reviews for Student_ID = 1
filtered_data = [review for review in data if review.get("PositionID") == 1]

# Display the filtered review
if filtered_data:
    # Assuming there's only one review for Student_ID = 1
    review = filtered_data[0]
    review_id = review.get('ReviewID', 'N/A')
    date = review.get('Date', 'N/A')
    culture = review.get('Culture', 'N/A')
    satisfaction = review.get('Satisfaction', 'N/A')
    compensation = review.get('Compensation', 'N/A')
    learning_opportunity = review.get('LearningOpportunity', 'N/A')
    work_life_balance = review.get('WorkLifeBalance', 'N/A')
    summary = review.get('Summary', 'N/A')
    position_id = review.get('PositionID', 'N/A')

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
            <div style="position: absolute; top: 10px; right: 15px; font-size: 14px; color: #555;">
                <strong>{date}</strong>
            </div>
            <h4 style="margin: 0; font-size: 20px;">Review ID: {review_id}</h4>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Culture:</strong> {culture}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Satisfaction:</strong> {satisfaction}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Compensation:</strong> {compensation}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Learning Opportunity:</strong> {learning_opportunity}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Work-Life Balance:</strong> {work_life_balance}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Summary:</strong> {summary}</p>
            <p style="font-size: 16px; margin: 10px 0 0 0;"><strong>Position ID:</strong> {position_id}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("No reviews found for PositionID = 1.")

        
        