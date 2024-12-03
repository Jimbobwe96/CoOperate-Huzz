import streamlit as st
import logging
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="CoOperate", layout="wide")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Header section
header_col1, header_col3 = st.columns([1, 1])

with header_col1:
    st.markdown("<h3 style='margin: 0;'>CoOperate</h3>", unsafe_allow_html=True)

with header_col3:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; justify-content: flex-end;">
            <a href="/" style="text-decoration: none;">
                <div style="
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    background-color: white;
                    font-weight: normal;
                    text-align: center;
                    color: black;
                    box-shadow: none;
                ">
                    Sign Out
                </div>
            </a>
            <a href="Student_Profile" style="text-decoration: none;">
                <img src="https://img.icons8.com/ios-filled/50/000000/user.png" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%; border: 1px solid #ccc;">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Divider
st.markdown("---")

# Check session state to handle navigation
page = st.session_state.page

if page == 'Home':
    # Main content for the Home page
    col_left, col_right = st.columns([2, 1])

    # Left column: Slightly smaller static image
    with col_left:
        st.image(
            "https://static1.gensler.com/uploads/hero_element/20772/thumb_desktop/thumbs/221201_US-Workplace-Survey_1_1669939238_1024x576.jpg",
            use_container_width=True,
            caption="Helping students achieve their goals",
            width=500,  # Reduced image width
        )

    # Decrease gap between image and reviews
    st.markdown("<div style='margin-bottom: 5px;'></div>", unsafe_allow_html=True)

    # Right column: Featured Reviews centered with text
    with col_right:
        st.markdown("<h4 style='font-size: 24px; text-align: center;'>Featured Reviews</h4>", unsafe_allow_html=True)

        data = {} 
        try:
            data = requests.get('http://api:4000/r/reviews').json()
        except:
            st.write("**Important**: Could not connect to sample api, so using dummy data.")
            data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

        # Simulated response data extracted via the GET route
        data = {
            "summary": ["Text 1", "Great!!!", "Phenom"]
        }

        # Display the data as text with dynamic review titles and styled boxes
        for index, item in enumerate(data["summary"]):
            review_title = f"Review {index + 1}"
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 15px;
                    margin: 10px auto; 
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                ">
                    <h4 style="margin: 0; font-size: 20px;">{review_title}</h4>
                    <p style="font-size: 16px; margin: 10px 0 0 0;">{item}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Footer with "All Reviews" link
    st.markdown("---")
    if st.button('All Reviews', 
            type = 'secondary', 
            use_container_width=False):
        st.switch_page('pages/Student_All_Reviews.py')


elif page == 'Company_Profile':
    # Import and display the Company_Profile page
    # Ensure Company_Profile.py is in the same directory
    import Company_Profile as cp
    cp.display_profile()

else:
    st.error("Page not found.")
