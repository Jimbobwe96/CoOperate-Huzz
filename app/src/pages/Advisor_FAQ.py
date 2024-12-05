import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Internship Advisor - Answer Questions", 
    page_icon="❓", 
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

    /* FAQ styling */
    .faq-container {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }

    .faq-container h2 {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
        text-align: center;
    }

    .faq-container .expander {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .faq-container .expander:hover {
        transform: scale(1.02);
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

# Page title
st.markdown("<h2 class='faq-container'>Answer Student Questions</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p style="text-align:center; color: rgba(255, 255, 255, 0.8);">
    This section allows you to address common questions students may have about internships.
    </p>
    """,
    unsafe_allow_html=True,
)

# FAQs Section
st.markdown("<div class='faq-container'>", unsafe_allow_html=True)
st.subheader("Frequently Asked Questions")

sample_questions = [
    "What is the process to apply for an internship?",
    "How do I prepare for my internship interview?",
    "Can I switch internships mid-way if it's not a good fit?",
    "What is the expected duration of most internships?",
    "Are internships paid or unpaid?"
]

# Display FAQs with expander style
for i, question in enumerate(sample_questions, 1):
    with st.expander(f"Q{i}: {question}", expanded=False):
        st.text_area(
            label=f"Response to: {question}",
            value="Type your answer here...",
            key=f"faq_response_{i}"
        )
st.markdown("</div>", unsafe_allow_html=True)
