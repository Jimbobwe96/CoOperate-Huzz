import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Admin - Home",
    page_icon="🔧",
    layout="wide"
)

# Function to handle sign-out redirection
def sign_out():
    # Clear any session state if applicable
    st.session_state.clear()
    # Redirect to the home page
    st.switch_page('Home.py')  # Ensure 'Home.py' exists and is correctly named in the pages directory

st.session_state['admin_id'] = 1

# Apply custom CSS for styling with an animated gradient background
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    /* Full-page gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Roboto', sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header styling */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 50px;
    }

    .header .title {
        font-size: 3rem;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
    }

    /* Sign Out button styling */
    .signout-button > div > button {
        background: rgba(255, 255, 255, 0.3);
        color: #ffffff;
        padding: 10px 20px;
        font-size: 1.2rem;
        font-weight: bold;
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.3s ease;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }

    .signout-button > div > button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.5);
    }

    /* Content section styling */
    .content {
        padding: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 30px;
    }

    /* Admin Card Styling */
    .admin-card {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        width: 250px;
        margin: 20px;
        padding: 30px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .admin-card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.4);
    }

    .admin-card h3 {
        font-size: 1.8rem;
        color: #ffffff;
        margin-bottom: 20px;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    /* Streamlit buttons within admin-card */
    .admin-card > div > button {
        background: #1ABC9C;
        color: #ffffff;
        padding: 10px 20px;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-family: 'Roboto', sans-serif;
    }

    .admin-card > div > button:hover {
        background-color: #16A085;
    }

    /* Responsive Design */
    @media (max-width: 1024px) {
        .admin-card {
            width: 45%;
        }
    }

    @media (max-width: 768px) {
        .header {
            flex-direction: column;
            align-items: flex-start;
        }

        .signout-button {
            margin-top: 10px;
        }

        .admin-card {
            width: 100%;
        }

        .content {
            padding: 30px;
            gap: 20px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header Section with Title and Sign Out Button using Streamlit's columns
header_col1, header_col2 = st.columns([3, 1], gap='small')

with header_col1:
    st.markdown("<h2 style='text-align: left; font-weight: bold; color: #000000;'>CoOperate Admin Page</h2>", unsafe_allow_html=True)

with header_col2:
    # Streamlit's button for Sign Out
    if st.button("Sign Out 🔓"):
        sign_out()

# Main Content Section with Admin Tools
st.markdown('<div class="content">', unsafe_allow_html=True)

# Create a Streamlit columns layout for admin tools (e.g., 4 tools => 4 columns)
admin_cols = st.columns(3, gap='medium')  # Adjust the number based on the number of tool


# Admin Tool 2: Flagged Reviews
with admin_cols[0]:
    st.markdown(f"""
        <div class="admin-card">
            <h3>🚩 Flagged Reviews</h3>
            <div>
    """, unsafe_allow_html=True)
    if st.button("Go to Flagged Reviews"):
        st.switch_page("pages/Admin_Flag_Review.py")  # Ensure this page exists without the '.py' extension
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

# Admin Tool 3: All Reviews
with admin_cols[1]:
    st.markdown(f"""
        <div class="admin-card">
            <h3>📝 All Reviews</h3>
            <div>
    """, unsafe_allow_html=True)
    if st.button("Go to All Reviews"):
        st.switch_page('pages/Admin_Review_Check.py')  # Updated Redirect as per your request
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

# Admin Tool 4: Activity Log
with admin_cols[2]:
    st.markdown(f"""
        <div class="admin-card">
            <h3>📜 Activity Log</h3>
            <div>
    """, unsafe_allow_html=True)
    if st.button("Go to Activity Log"):
        st.switch_page("pages/Admin_Activity.py")  # Ensure this page exists without the '.py' extension
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
