import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="CoOperate", layout="wide")
st.session_state['student_id'] = 1

# Add custom CSS for styling
st.markdown(
    """
    <style>
    /* Gradient background for the page */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header styling */
    h1 {
        font-size: 36px;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    /* Sign out button */
    .signout {
        display: inline-block;
        padding: 10px 20px;
        border: 1px solid #ffffff;
        border-radius: 5px;
        background-color: rgba(0, 0, 0, 0.2);
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .signout:hover {
        background-color: rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }

    /* Featured reviews card */
    .review-card {
        border: 1px solid #ffffff;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        background-color: rgba(255, 255, 255, 0.2);
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }

    .review-card h4 {
        margin: 0;
        font-size: 20px;
        color: #ffffff;
        text-align: center;
    }

    .review-card p {
        font-size: 16px;
        margin: 10px 0 0 0;
        color: #ffffff;
        text-align: center;
    }

    /* Footer link */
    .footer-link {
        font-size: 20px;
        font-weight: bold;
        text-decoration: none;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        transition: color 0.3s ease;
    }

    .footer-link:hover {
        color: #fbc2eb;
    }

    /* Co-op button */
    .coop-button {
        display: inline-block;
        padding: 15px 30px;
        text-decoration: none;
        font-size: 20px;
        color: #ffffff;
        font-weight: bold;
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid #ffffff;
        border-radius: 10px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    }

    .coop-button:hover {
        background-color: rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
header_col1, header_col3 = st.columns([1, 1])

with header_col1:
    st.markdown("<h1>CoOperate</h1>", unsafe_allow_html=True)

with header_col3:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 15px; justify-content: flex-end;">
            <a href="/" target="_self" class="signout">Sign Out</a>
            <a href="/Student_Profile" target="_self" style="text-decoration: none;">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/user.png" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid #ffffff; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Divider
st.markdown("<hr style='border: 1px solid #ffffff; margin: 20px 0;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    # Display a large image at the top
    st.image(
        "https://bpb-us-e1.wpmucdn.com/sites.northeastern.edu/dist/c/979/files/2022/05/2x3-campus-feature-42.jpg",
        caption="Explore Opportunities",
        use_container_width=True
    )


with col2:
    # Right column: Featured Reviews
    st.markdown("<h3 style='text-align: center;'>Featured Reviews</h3>", unsafe_allow_html=True)

    # Fetch data from the API or use dummy data if the request fails
    try:
        data = requests.get('http://api:4000/r/reviews').json()
    except:
        st.write("**Important**: Could not connect to sample API, so using dummy data.")
        data = [
            {"ReviewID": "1", "Summary": "Great learning environment!"},
            {"ReviewID": "2", "Summary": "Supportive team and good work-life balance."},
            {"ReviewID": "3", "Summary": "Excellent mentorship opportunities."},
        ]

    # Display reviews in a formatted way
    if isinstance(data, list):
        for review in data[:3]:  # Show only the first 3 reviews
            st.markdown(
                f"""
                <div class="review-card">
                    <h4>Review {review.get('ReviewID', 'N/A')}</h4>
                    <p>{review.get('Summary', 'N/A')}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Divider
    st.markdown("<hr style='border: 1px solid #ffffff; margin: 20px 0;'>", unsafe_allow_html=True)

    # Footer with buttons aligned horizontally
    st.markdown(
        """
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
            <a href="/Student_Coop_List" target="_self" class="coop-button">Saved Co-op List</a>
            <a href="/Student_All_Reviews" target="_self" class="coop-button">View All Reviews →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
