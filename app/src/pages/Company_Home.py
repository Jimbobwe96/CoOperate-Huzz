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

# Apply custom CSS for styling
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Navigation Bar */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 30px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }

    .top-bar h3 {
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
        margin: 0;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    .top-bar button {
        font-size: 1rem;
        font-weight: bold;
        padding: 10px 20px;
        background: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        cursor: pointer;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .top-bar button:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
    }

    /* Main Content Styling */
    .content {
        padding: 30px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        color: #ffffff;
    }

    .content h2 {
        font-size: 2rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    .content button {
        font-size: 1.5rem; /* Larger font size */
        font-weight: bold;
        padding: 20px 40px; /* Bigger buttons */
        background: rgba(255, 255, 255, 0.2); /* Translucent background */
        color: #ffffff; /* Bright white text */
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.6);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px; /* Rounded corners */
        cursor: pointer;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        width: 100%; /* Full-width buttons */
        max-width: 400px; /* Limit width for readability */
    }

    .content button:hover {
        background: rgba(255, 255, 255, 0.4); /* Highlight on hover */
        transform: scale(1.1); /* Subtle hover effect */
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 30px;
        opacity: 0.8;
    }

    .footer a {
        color: #ffffff;
        text-decoration: underline;
    }

    .footer a:hover {
        color: #f0f0f0;
    }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
    <div class="top-bar">
        <h3>Company Dashboard</h3>
    </div>
""", unsafe_allow_html=True)

# Sign Out Button
if st.button("Sign Out"):
    sign_out()

# Main Content
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

# Footer
st.markdown("""
    <div class="footer">
        Powered by <a href="/">Company Dashboard</a>. Designed for seamless management.
    </div>
""", unsafe_allow_html=True)
