import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Company Dashboard",
    page_icon="🏢",
    layout="wide"
)

# Function to handle sign-out redirection
def sign_out():
    # Clear any session state if applicable
    st.session_state.clear()
    # Redirect to the home page
    st.switch_page("Home.py")

# Apply custom CSS for styling with the animated theme
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

    /* Translucent button styling */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.3);
        color: #ffffff;
        padding: 20px 40px;
        margin: 15px 0;
        font-size: 1.8rem;
        font-weight: bold;
        width: 100%;
        border: 1px solid rgba(255, 255, 255, 0.4);
        cursor: pointer;
        border-radius: 12px;
        transition: transform 0.2s ease, box-shadow 0.3s ease;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }

    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.5);
    }

    /* Content section */
    .content {
        padding: 30px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        color: #ffffff;
    }

    .content h2 {
        font-size: 2rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    </style>
""", unsafe_allow_html=True)

# Header with animation overlay
st.markdown("""
    <div class="title">Company Dashboard</div>
    <div class="subtitle">Manage your company profile and job postings seamlessly</div>
""", unsafe_allow_html=True)

# Main Content Section
st.markdown('<div class="content">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Left Column: Company Profile
with col1:
    st.markdown("<h2>Company Profile</h2>", unsafe_allow_html=True)
    st.text_area("Add company details here...", height=200)
    if st.button("Edit Profile"):
        st.write("Edit profile functionality coming soon!")
    if st.button("Delete Profile"):
        st.write("Delete profile functionality coming soon!")

# Right Column: Job Postings
with col2:
    st.markdown("<h2>Job Postings</h2>", unsafe_allow_html=True)
    job_buttons = ["Software Developer", "Data Scientist", "Project Manager"]
    for job in job_buttons:
        if st.button(job):
            st.write(f"Redirecting to details about {job}...")

st.markdown('</div>', unsafe_allow_html=True)

# Sign Out Button
if st.button("Sign Out"):
    sign_out()
