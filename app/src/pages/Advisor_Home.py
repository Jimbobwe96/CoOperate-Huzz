import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Co-op Advisor - Home", 
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
        src="https://media.istockphoto.com/id/1278975231/photo/professor-helping-student-during-computer-class.jpg?s=612x612&w=0&k=20&c=tWPEUG8Nodw3g7kC_SbB8Zl--N8AuUPaGFEVUNKYyfM=" 
        class="image" 
        alt="Helping Students Achieve their Goals!" />
        """, 
        unsafe_allow_html=True
    )

# Right column: Buttons and title
with col_2:
    st.markdown(
    "<div style='text-align: center; font-size: 24px; font-weight: bold;'>Advisor Tools</div>", 
    unsafe_allow_html=True
    )
    st.markdown("   ")

    if st.button("Answer Student Questions",             
                type = 'secondary', 
                use_container_width=True):
        st.switch_page("pages/Advisor_FAQ.py")

    st.markdown("  ")  # Spacer

    if st.button("Compatibility Assessment", 
                type = 'secondary', 
                use_container_width=True):
        st.switch_page("pages/Advisor_Comp.py")
