# Google.py

import streamlit as st

st.set_page_config(page_title="Google", layout="wide")
def display_google_profile():

    # Header section
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <h3 style="margin: 0;">CoOperate</h3>
            <div style="display: flex; align-items: center; gap: 10px;">
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
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Divider
    st.markdown("---")

    # Company Logo and Name
    st.image("https://logos-world.net/wp-content/uploads/2020/09/Google-Logo.png", width=200)
    st.markdown("# Google LLC")

    # Company Description
    st.markdown(
        """
        **Industry:** Technology

        **About Google:**
        Google LLC is an American multinational technology company specializing in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware.

        **Mission:**
        To organize the world's information and make it universally accessible and useful.

        **Founded:** September 4, 1998

        **Founders:** Larry Page, Sergey Brin

        **Headquarters:** Mountain View, California, United States
        """
    )

    # Key Company Metrics
    st.markdown("## Key Metrics")
    st.markdown(
        """
        - **Number of Employees:** Over 135,000
        - **Revenue:** $182.5 billion (2020)
        - **Subsidiaries:** YouTube, Fitbit, Waymo, and more
        """
    )

    # Company Culture and Values
    st.markdown("## Company Culture and Values")
    st.markdown(
        """
        Google's culture is defined by its emphasis on innovation, collaboration, and a commitment to diversity and inclusion. The company encourages its employees to think big and take risks, fostering an environment where new ideas can thrive.

        **Core Values:**
        - Focus on the user and all else will follow.
        - It's best to do one thing really, really well.
        - Fast is better than slow.
        - Great just isn't good enough.
        """
    )

    # Current Job Openings (Sample)
    st.markdown("## Current Job Openings")
    job_listings = [
        {"title": "Software Engineer", "location": "Mountain View, CA"},
        {"title": "Product Manager", "location": "New York, NY"},
        {"title": "Data Scientist", "location": "Seattle, WA"},
    ]

    for job in job_listings:
        st.markdown(f"- **{job['title']}** - {job['location']}")

    # Footer
    st.markdown("---")
    st.markdown("For more information, visit [Google Careers](https://careers.google.com/).")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.page = 'Home'
