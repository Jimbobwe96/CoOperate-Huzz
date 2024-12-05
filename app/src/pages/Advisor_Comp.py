import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Internship Advisor - Compatibility Assessment",
    page_icon="📊",
    layout="wide"
)

# Apply custom CSS for the theme
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header styling */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        margin-bottom: 30px;
    }

    .header-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.6);
    }

    .header-buttons {
        display: flex;
        gap: 15px;
    }

    .home-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: bold;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 25px;
        text-align: center;
        text-decoration: none;
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .home-button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }

    /* Form styling */
    .form-container {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-top: 20px;
    }

    .form-container h2 {
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
        text-transform: uppercase;
    }

    .form-container input, .form-container textarea {
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 5px;
        padding: 10px;
        width: 100%;
        margin-bottom: 15px;
        font-size: 1rem;
    }

    .form-container input::placeholder, .form-container textarea::placeholder {
        color: rgba(255, 255, 255, 0.7);
    }

    .form-container button {
        display: block;
        font-size: 1rem;
        font-weight: bold;
        padding: 15px 30px;
        margin: 20px auto;
        background-color: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #ffffff;
        border-radius: 25px;
        text-align: center;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .form-container button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section with Home button
st.markdown(
    """
    <div class="header">
        <div class="header-title">Internship Advisor</div>
        <div class="header-buttons">
            <a href="/" target="_self" class="home-button">🏠 Home</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Form container
st.markdown(
    """
    <div class="form-container">
        <h2>Compatibility Assessment</h2>
    """,
    unsafe_allow_html=True,
)

# Compatibility form
name = st.text_input("👤 Student Name", placeholder="Enter student name here")
skills = st.text_area("📜 List of Skills", placeholder="List key skills (e.g., programming, teamwork)")
preferences = st.text_area("📍 Internship Preferences", placeholder="Enter preferences (e.g., location, type of role)")

if st.button("🔍 Assess Compatibility"):
    if name.strip():
        st.success(f"Assessing compatibility for **{name}**...")
        # Placeholder for assessment logic
        st.info("Results: Based on the provided details, the student matches well with internships in [Placeholder].")
    else:
        st.error("Please provide a valid student name before assessing compatibility.")

st.markdown("</div>", unsafe_allow_html=True)
