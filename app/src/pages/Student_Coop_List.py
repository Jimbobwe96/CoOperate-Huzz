import streamlit as st
import pandas as pd
import requests

# Page configuration
st.set_page_config(page_title="Your saved Co-op List", layout="wide")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    /* Gradient background for the page */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header styling */
    h1 {
        font-size: 36px;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    /* Back button styling */
    .back-button {
        display: inline-block;
        padding: 10px 20px;
        border: 1px solid #ffffff;
        border-radius: 5px;
        background-color: rgba(0, 0, 0, 0.2);
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .back-button:hover {
        background-color: rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }

    /* Table styling */
    .styled-table th, .styled-table td {
        text-align: center;
        padding: 8px;
        font-size: 16px;
        background: rgba(0, 0, 0, 0.2);
        border-bottom: 1px solid #ffffff;
    }

    .styled-table th {
        font-weight: bold;
        color: #ffffff;
    }

    .styled-table td {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
st.markdown("<h1>Your saved Co-ops</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #ffffff; margin: 20px 0;'>", unsafe_allow_html=True)

# Fetch the Co-op list data from the API
student_id = st.session_state.get('student_id', 1)  # Replace with logic to retrieve the correct student ID
api_url = f"http://api:4000/cl/coop_list/student/{student_id}"

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()

    # Ensure the data is a list of dictionaries
    if isinstance(data, list) and len(data) > 0:
        CoopList = pd.DataFrame(data)
    else:
        CoopList = pd.DataFrame(columns=["Title", "Name", "City"])  # Fallback if data is empty or malformed
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch data from API: {e}")
    CoopList = pd.DataFrame(columns=["Title", "Name", "City"])

# Display the table if CoopList is not empty
if not CoopList.empty:
    st.markdown(
        CoopList.style.set_table_attributes('class="styled-table"').to_html(index=False),
        unsafe_allow_html=True
    )
else:
    st.warning("No Co-op data available for this student.")

# Back button
st.markdown(
    """
    <div style="text-align: center;">
        <a href="/" class="back-button">← Back</a>
    </div>
    """,
    unsafe_allow_html=True,
)



