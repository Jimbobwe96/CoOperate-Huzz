import streamlit as st

# Top navigation bar with Home button and logo
col1, col2 = st.columns([9, 1])  # Adjust proportions as needed

with col1:
    st.markdown("""
        <style>
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            margin-bottom: 20px;
        }
        .top-bar h1 {
            margin: 0;
            font-size: 1.5em;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
        }
        .top-bar img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }
        /* Remove spacing between buttons */
        .button-row .stButton button {
            margin: 0;  /* Remove margins */
            padding: 8px 16px;  /* Adjust padding if needed */
        }
        .button-row .stButton {
            margin: 0;  /* Remove margins around stButton containers */
        }
        </style>
        <div class="top-bar">
            <h1>CoOperate</h1>
        </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button('Sign Out', 
                 type='secondary', 
                 use_container_width=False):
        st.switch_page('Home.py')

# Main content layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Company Profile")
    st.text_area("Add company details here...", height=200)
    
    # Use a container with CSS class for styling
    with st.container():
        st.markdown('<div class="button-row">', unsafe_allow_html=True)
        # Place buttons side by side using columns
        button_col1, button_col2 = st.columns([1, 1])
        with button_col1:
            st.button("Edit Profile", key='edit_profile')
        with button_col2:
            st.button("Delete Profile", key='delete_profile')
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("Job Postings")
    if st.button('Software Developer', 
                 type='secondary', 
                 use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
    st.write(" ") 
    if st.button('Data Scientist', 
                 type='secondary', 
                 use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
    st.write(" ")
    if st.button('John', 
                 type='secondary', 
                 use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
