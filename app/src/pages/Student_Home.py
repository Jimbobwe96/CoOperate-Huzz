import streamlit as st
import logging
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(page_title="CoOperate", layout="wide")

# Header section
header_col1, header_col3 = st.columns([1, 1])

with header_col1:
    st.markdown("<h3 style='margin: 0;'>CoOperate</h3>", unsafe_allow_html=True)

with header_col3:
        st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; justify-content: flex-end;">
            <a href="/" target="_self" style="text-decoration: none;">
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
            <a href="/Student_Profile" target="_self" style="text-decoration: none;">
                <img src="https://img.icons8.com/ios-filled/50/000000/user.png" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%; border: 1px solid #ccc;">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Divider
st.markdown("---")




    # Main content for the Home page
col_left, col_right = st.columns([2, 1])

    # Left column: Slightly smaller static image
with col_left:
        st.image(
            "https://static1.gensler.com/uploads/hero_element/20772/thumb_desktop/thumbs/221201_US-Workplace-Survey_1_1669939238_1024x576.jpg",
            use_container_width=True,
            caption="Helping Students Find Great Co-Ops!",
            width=500,  # Reduced image width
        )

    # Decrease gap between image and reviews
st.markdown("<div style='margin-bottom: 5px;'></div>", unsafe_allow_html=True)

    # Right column: Featured Reviews centered with text
with col_right:
        st.markdown(
        "<h3 style='margin: 0; text-align: center; font-weight: bold; font-size: 150%;'>Featured Reviews</h3>",
        unsafe_allow_html=True
)

        # Fetch data from the API or use dummy data if the request fails
        try:
            data = requests.get('http://api:4000/r/reviews').json()
        except:
            st.write("**Important**: Could not connect to sample api, so using dummy data.")
            data = {
                "a":{"b": "123", "c": "hello"},
                "z": {"b": "456", "c": "goodbye"}}

        # Display reviews from the data fetched
        limited_reviews = data[:3]
        if isinstance(data, list): 
            for review in limited_reviews:
                review_id = review.get('ReviewID', 'N/A')
                student_id = review.get('StudentID', 'N/A')
                date = review.get('Date', 'N/A')
                culture = review.get('Culture', 'N/A')
                satisfaction = review.get('Satisfaction', 'N/A')
                compensation = review.get('Compensation', 'N/A')
                learning_opportunity = review.get('LearningOpportunity', 'N/A')
                work_life_balance = review.get('WorkLifeBalance', 'N/A')
                summary = review.get('Summary', 'N/A')
                flagged = review.get('Flagged', 'N/A')
                resolved_by = review.get('ResolvedBy', 'N/A')
                position_id = review.get('PositionID', 'N/A')

                # Display in a formatted way
                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        padding: 15px;
                        margin: 10px auto; 
                        background-color: #f9f9f9;
                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    ">
                        <h4 style="margin: 0; font-size: 20px; text-align: center;">Review {review_id}</h4>
                        <p style="font-size: 16px; margin: 10px 0 0 0; text-align: center;"><strong></strong> {summary}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# Footer with "All Reviews" linked text
st.markdown("---")
st.markdown(
        """
        <div style="text-align: left; margin-top: 20px;">
            <a href="/Student_All_Reviews" target="_self" style="text-decoration: none; font-size: 24px; color: #000000; font-weight: bold;">
                All Reviews
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
