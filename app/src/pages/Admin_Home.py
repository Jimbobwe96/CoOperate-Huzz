import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin - Home", layout="wide")

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
    .image {
        max-height: 900px;
        width: 1100px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Page title
col1, col2 = st.columns([25, 2]) 
with col1:
    st.markdown('<div class="title">Co-op Advisor Portal</div>', unsafe_allow_html=True)
with col2:
    if st.button('Sign Out', type='secondary', use_container_width=False):
        st.switch_page('Home.py')

col_1, col_2 = st.columns([2, 1])

# Left column: Static image
with col_1:
    st.markdown(
        """
        <img 
        src="https://exclusive.multibriefs.com/images/exclusive/0804principal.jpg" 
        class="image" 
        alt="Ensuring a Safe Platform for Students!" />
        """, 
        unsafe_allow_html=True
    )

# Right column: Buttons and title
with col_2:
    st.markdown(
    "<div style='text-align: center; font-size: 24px; font-weight: bold;'>Admin Tools</div>", 
    unsafe_allow_html=True
    )
    st.markdown("   ")

    if st.button("Aggregated Scores",             
                type = 'secondary', 
                use_container_width=True):
        st.switch_page("pages/Admin_Agg_Score.py")

    st.markdown("  ")  # Spacer

    if st.button("Flagged Reviews", 
                type = 'secondary', 
                use_container_width=True):
        st.switch_page("pages/Admin_Flag_Review.py")

    if st.button("All Reviews", 
                type = 'secondary', 
                use_container_width=True):
        st.switch_page("pages/Admin_Flag_Review.py")
