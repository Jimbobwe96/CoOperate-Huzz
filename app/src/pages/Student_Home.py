import streamlit as st

# Page configuration
st.set_page_config(page_title="CoOperate", layout="wide")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Function to handle search input
def handle_search():
    query = st.session_state['search_input'].lower()
    if query == 'google':
        # Set session state to navigate to Google page
        st.session_state.page = 'pages/Google.py'
        # No need to rerun or set query params

# Header section with functional search bar
header_col1, header_col2, header_col3 = st.columns([1, 2, 1])

with header_col1:
    st.markdown("<h3 style='margin: 0;'>CoOperate</h3>", unsafe_allow_html=True)

with header_col2:
    search_input = st.text_input("", placeholder="Search for reviews...", key='search_input', on_change=handle_search)

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

        review_style = """
            <div style="
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 30px;
                margin: 20px auto; 
                width: 90%;
                background-color: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            ">
                <p style="font-size: 20px; text-align: center; margin: 0;"><strong>{title}</strong>: {content}</p>
            </div>
        """

        # Review 1
        st.markdown(
            review_style.format(title="Review 1", content="Great platform for students!"),
            unsafe_allow_html=True,
        )

        # Gap between reviews
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

        # Review 2
        st.markdown(
            review_style.format(title="Review 2", content="Helped me secure my first internship!"),
            unsafe_allow_html=True,
        )

        # Gap between reviews
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

        # Review 3
        st.markdown(
            review_style.format(title="Review 3", content="Easy to navigate and resourceful!"),
            unsafe_allow_html=True,
        )

    # Footer links
    st.markdown("---")
    st.markdown("<h5>Hotlinks to Helpful Resources</h5>", unsafe_allow_html=True)

elif page == 'Google':
    # Display the Google company profile page
    # Ensure Google.py is in the same directory and contains the display_google_profile function
    import Google
    Google.display_google_profile()

else:
    st.error("Page not found.")
