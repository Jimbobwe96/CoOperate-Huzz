import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Internship Advisor - Home", 
    page_icon="🌐", 
    layout="wide"
)

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C3E50;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #34495E;
        margin-bottom: 20px;
    }
    .button {
        font-size: 1rem;
        font-weight: bold;
        padding: 10px 20px;
        background-color: #1ABC9C;
        border: none;
        color: white;
        border-radius: 5px;
        margin-top: 10px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #16A085;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Page title
st.markdown('<div class="title">Co-op Advisor Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to the Co-op Advisor! Navigate through the options below to assist students with their Co-op-related needs.</div>', unsafe_allow_html=True)

# Create a container for buttons with padding
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("Answer Student Questions", key="faq_button"):
            st.switch_page("pages/Advisor_FAQ.py")
    
    with col2:
        if st.button("Compatibility Assessment", key="comp_button"):
            st.switch_page("pages/Advisor_Comp.py")
    
    with col3:
        if st.button("Sign Out", key="signout_button"):
            st.switch_page("Home.py")
