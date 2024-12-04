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
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# ***************************************************
#    The major content of this page
# ***************************************************

logger.info("Loading the Home page of the app")

# Adding custom CSS and JavaScript for animations and smooth transitions
st.markdown(
    """
    <style>
    /* Full-page gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hide main content until animation is done */
    .main-content {
        display: none;
        opacity: 0;
        animation: fadeInContent 2s ease-in forwards;
        animation-delay: 4s;
    }

    @keyframes fadeInContent {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Overlay container (starts black) */
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: black;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: white;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        animation: fadeOut 1.5s ease-in-out forwards;
        animation-delay: 3.5s;
    }

    /* Overlay animations */
    .overlay h1 {
        font-size: 4rem;
        animation: zoomIn 1.5s ease-out forwards;
        margin: 0;
    }

    .overlay p {
        font-size: 1.5rem;
        margin-top: 1rem;
        opacity: 0;
        animation: fadeIn 2s ease-out forwards;
        animation-delay: 1.5s;
    }

    @keyframes zoomIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; visibility: hidden; }
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

    /* Translucent button styling */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.2); /* Translucent white */
        color: white;
        padding: 20px;
        margin: 10px 0;
        font-size: 1.5rem;
        width: 100%;
        border: 1px solid rgba(255, 255, 255, 0.3);
        cursor: pointer;
        border-radius: 10px;
        transition: transform 0.2s ease, box-shadow 0.3s ease;
        font-family: 'Roboto', sans-serif;
    }

    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.3);
    }
    </style>

    <script>
    // JavaScript to reveal main content after overlay fades out
    document.addEventListener("DOMContentLoaded", function() {
        setTimeout(() => {
            const mainContent = document.querySelector('.main-content');
            if (mainContent) {
                mainContent.style.display = 'block';
            }
        }, 4000); // Matches fade-out and fade-in timing
    });
    </script>
    """,
    unsafe_allow_html=True
)

# HTML for the opening animation overlay
st.markdown(
    """
    <div class="overlay">
        <h1>CoOperate</h1>
        <p>Unleashing Potential Together</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Main content (initially hidden)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Display the title and subtitle
st.markdown('<h1 class="title">Welcome to CoOperate</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Connecting Students, Advisors, Companies, and Administrators</p>', unsafe_allow_html=True)

# Create full-width buttons
if st.button("Act as a Student", key="student"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'John'
    logger.info("Logging in as a Student")
    st.experimental_rerun()

if st.button("Act as a Co-Op Advisor", key="advisor"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'coop_advisor'
    st.session_state['first_name'] = 'Mohammad'
    st.experimental_rerun()

if st.button("Act as a Company", key="company"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'Google'
    st.experimental_rerun()

if st.button("Act as an Admin", key="admin"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Admin'
    st.session_state['admin_id'] = 1
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
