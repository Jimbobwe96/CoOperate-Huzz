import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Company Dashboard",
    page_icon="🏢",
    layout="wide"
)

col1, col2 = st.columns([10, 2])
with col2:
    if st.button('Home', 
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
    st.text_area("Add company details here...", height=200)
    if st.button("Edit Profile"):
        st.write("Edit profile functionality coming soon!")
    if st.button("Delete Profile"):
        st.write("Delete profile functionality coming soon!")

# Right Column: Job Postings
with col2:
    st.markdown("<h2>Job Postings</h2>", unsafe_allow_html=True)
    if st.button("Job 1"):
        st.switch_page('pages/Job_Posting.py')



