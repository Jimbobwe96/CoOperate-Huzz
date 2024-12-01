import streamlit as st

# Page configuration
st.set_page_config(page_title="CoOperate", layout="wide")

# Define a function for navigation
def navigate_to(page_name):
    st.session_state["page"] = page_name

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Header section
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
        <h3 style="margin: 0;">CoOperate</h3>
        <input type="text" placeholder="Search for reviews..." style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 60%;">
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
                    Home
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

# Main content
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
            padding: 30px; /* Increased padding for larger height */
            margin: 20px auto; 
            width: 90%; /* Center reviews with the heading */
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
