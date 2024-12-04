##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the main Streamlit library
import streamlit as st

# Set page configuration for wide layout
st.set_page_config(layout='wide')

# Initialize authentication status
st.session_state['authenticated'] = False

# ***************************************************
#    The major content of this page
# ***************************************************

logger.info("Loading the Home page of the app")

# Adding custom CSS for an animated background and styling
st.markdown(
    """
    <style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
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
        font-size: 64px;
        color: #FFFFFF;
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px #000000;
    }
    /* Subtitle styling */
    .subtitle {
        font-size: 24px;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 1px 1px #000000;
    }
    /* Content centering */
    .content {
        text-align: center;
    }
    /* Icon styling */
    .icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px #000000;
    }
    /* Button styling */
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.5em 1em;
        margin: 10px;
        font-size: 16px;
        border-radius: 10px;
        border: 2px solid white;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title and subtitle
st.markdown('<h1 class="title">Welcome to CoOperate</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Connecting Students, Advisors, Companies, and Administrators</p>', unsafe_allow_html=True)

# Create columns for user roles
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.image('https://via.placeholder.com/150/0000FF/FFFFFF?text=Student', use_column_width=False, width=150)
    if st.button("Act as a Student"):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'student'
        st.session_state['first_name'] = 'John'
        logger.info("Logging in as a Student")
        st.switch_page('pages/Student_Home.py')
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.image('https://via.placeholder.com/150/FF0000/FFFFFF?text=Advisor', use_column_width=False, width=150)
    if st.button("Act as a Co-Op Advisor"):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'coop_advisor'
        st.session_state['first_name'] = 'Mohammad'
        st.switch_page('pages/Advisor_Home.py')
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.image('https://via.placeholder.com/150/00FF00/FFFFFF?text=Company', use_column_width=False, width=150)
    if st.button("Act as a Company"):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'administrator'
        st.session_state['first_name'] = 'Google'
        st.switch_page('pages/Company_Home.py')
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.image('https://via.placeholder.com/150/FFFF00/FFFFFF?text=Admin', use_column_width=False, width=150)
    if st.button("Act as an Admin"):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'Admin'
        st.switch_page('pages/Admin_Home.py')
    st.markdown('</div>', unsafe_allow_html=True)
