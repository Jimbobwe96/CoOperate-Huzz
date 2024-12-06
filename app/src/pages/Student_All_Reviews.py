import logging
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Set up basic logging infrastructure
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="All Reviews", layout="wide", page_icon="⭐")

# Initialize authentication status if not present
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# ***************************************************
#    The major content of this page
# ***************************************************

logger.info("Loading the All Reviews page of the app")

# Adding custom CSS for styling
st.markdown(
    """
    <style>
    /* Full-page gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        font-family: 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header Styling */
    .header {
        padding: 20px 0;
        border-bottom: 2px solid rgba(255, 255, 255, 0.3);
    }
    .header h1 {
        font-size: 2.5rem;
        color: #000000;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        margin: 0;
    }

    /* Streamlit Button Styling Override */
    .custom-buttons {
        display: flex;
        gap: 15px;
    }
    .custom-buttons > button {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #000000;
        padding: 12px 24px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 1.2rem;
        font-weight: bold;
        transition: transform 0.2s ease, box-shadow 0.3s ease, background 0.3s ease;
        backdrop-filter: blur(3px);
        font-family: 'Roboto', sans-serif;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    .custom-buttons > button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.4);
    }

    /* Review Card Styling */
    .review-card {
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background: rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .review-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
    .review-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }
    .review-header h2 {
        margin: 0;
        font-size: 1.5rem;
        color: #000000;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    .review-date {
        font-size: 0.9rem;
        color: #000000;
    }
    .review-content p {
        margin: 5px 0;
        font-size: 1rem;
        color: #000000;
    }
    .review-content p strong {
        color: #000000;
    }

    /* Button Styling Override for Streamlit Buttons */
    .stButton > button {
        width: 100%;
        max-width: 300px;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .header-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        .custom-buttons {
            margin-top: 10px;
            width: 100%;
            flex-direction: column;
            gap: 10px;
        }
        .custom-buttons > button {
            width: 100%;
            max-width: none;
            margin-left: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Header Section using Streamlit Columns
header_cols = st.columns([3, 1])

with header_cols[0]:
    st.markdown('<div class="header"><h1>All Reviews</h1></div>', unsafe_allow_html=True)

with header_cols[1]:
    # Container for buttons with custom CSS class
    st.markdown('<div class="custom-buttons">', unsafe_allow_html=True)
    # My Reviews Button
    if st.button("My Reviews"):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'student'
        st.session_state['first_name'] = 'John'
        st.switch_page('pages/Student_My_Reviews.py')  # Use the exact page name defined in your multipage app
    # Sign Out Button
    if st.button("Home"):
        st.switch_page('pages/Student_Home.py')  # Use the exact page name defined in your multipage app
    st.markdown('</div>', unsafe_allow_html=True)

# Fetch data from the API or use dummy data if the request fails
try:
    response = requests.get('http://api:4000/r/reviews')
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    logger.info("Successfully fetched reviews from API.")
except Exception as e:
    logger.error(f"API connection failed: {e}")
    st.warning("**Important**: Could not connect to the sample API, so using dummy data.")
    data = [
        {
            "Company": "John Inc",
            "Title": "John",
            "Culture": 2,
            "Satisfaction": 2,
            "Compensation": 2,
            "LearningOpportunity": 2,
            "WorkLifeBalance": 2,
            "Summary": "Great experience",
            "Date": "2024-12-05"
        },
        {
            "Company": "Samuel Inc",
            "Title": "Sam",
            "Culture": 2,
            "Satisfaction": 5,
            "Compensation": 5,
            "LearningOpportunity": 5,
            "WorkLifeBalance": 5,
            "Summary": "Good learning curve",
            "Date": "2024-11-25"
        }
    ]

# Display reviews from the data fetched
if isinstance(data, list) and data:
    for review in data:
        company = review.get('Company', 'N/A')
        title = review.get('Title', 'N/A')
        culture = review.get('Culture', 'N/A')
        satisfaction = review.get('Satisfaction', 'N/A')
        compensation = review.get('Compensation', 'N/A')
        learning_opportunity = review.get('LearningOpportunity', 'N/A')
        work_life_balance = review.get('WorkLifeBalance', 'N/A')
        summary = review.get('Summary', 'N/A')
        date = review.get('Date', 'N/A')

        # Display in a visually appealing format
        st.markdown(
            f"""
            <div class="review-card">
                <div class="review-header">
                    <h2>{company}</h2>
                    <h3>{title}</h3>
                    <div class="review-date">{date}</div>
                </div>
                <div class="review-content">
                    <p><strong>Culture:</strong> {culture}</p>
                    <p><strong>Satisfaction:</strong> {satisfaction}</p>
                    <p><strong>Compensation:</strong> {compensation}</p>
                    <p><strong>Learning Opportunity:</strong> {learning_opportunity}</p>
                    <p><strong>Work-Life Balance:</strong> {work_life_balance}</p>
                    <p><strong>Summary:</strong> {summary}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("No reviews available to display.")

# Close Main Content Container
st.markdown('</div>', unsafe_allow_html=True)
