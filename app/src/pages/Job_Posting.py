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
        st.switch_page('pages/Company_Job_Postings.py')



# Fetch data from the API or use dummy data if the request fails
try:
    position_id = st.session_state['passed_position_id']
    logger.info(position_id)
    response = requests.get(f'http://api:4000/cr/coop_role/{position_id}')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {"Company": "Joe", "Role": "Joe", "Location": "MA", "Pay": 9999,
         "Required GPA": 3.0, "Culture": 3, "Satisfaction": 4,
         "Compensation": 2, "Learning": 2, "Work Life Balance": 1},
    ]

     # Loop through the list and display each review
if data:  
        for review in data:
            company = review.get('Company', 'N/A')
            role = review.get('Role', 'N/A')
            location = review.get('Location', 'N/A')
            pay = review.get('Pay', 'N/A')
            required_gpa = review.get('Required GPA', 'N/A')
            culture = review.get('Culture', 'N/A')
            satisfaction = review.get('Satisfaction', 'N/A')
            compensation = review.get('Compensation', 'N/A')
            learning = review.get('Learning', 'N/A')
            balance = review.get('Work Life Balance', 'N/A')

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
                                                                              
                </div>
                """,
                unsafe_allow_html=True
            ) 
            
            culture_score = (float(culture)/5.00)
            satisfaction_score = (float(satisfaction)/5.00)
            compensation_score = (float(compensation)/5.00)
            learning_score = (float(learning)/5.00)
            balance_score = (float(balance)/5.00)
            overall_score = (((float(culture) + float(satisfaction) + float(compensation) + float(learning) + float(balance)) / 5) / 5)

            st.write("Average Culture:" + culture)
            st.progress(culture_score)
            st.write("Average Satisfaction:" + satisfaction)
            st.progress(satisfaction_score)
            st.write("Average Compensation:" + compensation)
            st.progress(compensation_score)
            st.write("Average Learning:" + learning)
            st.progress(learning_score)
            st.write("Average Work Life Balance:" + balance)
            st.progress(balance_score)
            st.write("Overall Rating:" + str(overall_score * 5))
            st.progress(overall_score)

else:
        st.write("No data available to display.")
