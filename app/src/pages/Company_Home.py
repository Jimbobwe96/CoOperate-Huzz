import streamlit as st

# Initialize session state for company details
if "company_details" not in st.session_state:
    st.session_state["company_details"] = "Add company details here..."

# Function to handle editing
def edit_details():
    st.session_state["edit_mode"] = True

def save_details(new_details):
    st.session_state["company_details"] = new_details
    st.session_state["edit_mode"] = False

# Top navigation bar
col1, col2 = st.columns([12.5, 1])  # Adjust proportions as needed

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
        .button-row .stButton button {
            margin: 0;
            padding: 8px 16px;
        }
        .button-row .stButton {
            margin: 0;
        }
        </style>
        <div class="top-bar">
            <h3>CoOperate</h3>
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
    
    if "edit_mode" in st.session_state and st.session_state["edit_mode"]:
        # Editing mode
        new_details = st.text_area("Edit company details", 
                                   st.session_state["company_details"], 
                                   height=200)
        if st.button("Save"):
            save_details(new_details)
        if st.button("Cancel"):
            st.session_state["edit_mode"] = False
    else:
        # Display mode
        st.text_area("Company Details", 
                     st.session_state["company_details"], 
                     height=200, disabled=True)
        if st.button("Edit Profile", key='edit_profile'):
            edit_details()

    # Optionally add a delete button
    if st.button("Delete Profile", key='delete_profile'):
        st.session_state["company_details"] = "Add company details here..."

with col2:
    st.subheader("Job Postings")
    if st.button('Software Developer', type='secondary', use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
    st.write(" ") 
    if st.button('Data Scientist', type='secondary', use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
    st.write(" ")
    if st.button('John', type='secondary', use_container_width=True):
        st.switch_page('pages/Advisor_Home.py')
