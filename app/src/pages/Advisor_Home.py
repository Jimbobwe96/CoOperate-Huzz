import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Co-op Advisor Portal",
    page_icon="🌟",
    layout="wide"
)

# Apply custom CSS for a stunning design
st.markdown(
    """
    <style>
    /* Page gradient background */
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

    /* Title styling */
    .title {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 20px;
        text-align: center;
        text-transform: uppercase;
        color: #ffffff;
        letter-spacing: 3px;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.6);
    }

    /* Subtitle styling */
    .subtitle {
        font-size: 1.2rem;
        color: #f0f0f0;
        text-align: center;
        margin-bottom: 40px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    /* Card styling */
    .card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.5);
    }

    .card h3 {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
        text-align: center;
        text-transform: uppercase;
    }

    .card p {
        font-size: 1rem;
        color: #ffffff;
        text-align: center;
    }

    /* Buttons styling */
    .button {
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

    .button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }

    /* Footer styling */
    .footer {
        margin-top: 40px;
        text-align: center;
        font-size: 0.9rem;
        color: #ffffff;
        opacity: 0.8;
    }

    .footer a {
        color: #ffffff;
        text-decoration: underline;
    }

    .footer a:hover {
        color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title and subtitle
st.markdown('<div class="title">Co-op Advisor Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Empowering advisors to connect and guide students effectively</div>', unsafe_allow_html=True)

# Main content layout
col1, col2, col3 = st.columns(3)

# Card 1: Answer Student Questions
with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Answer Student Questions</h3>
            <p>Provide timely answers to student inquiries and guide them through their co-op journey.</p>
            <a href="/pages/Advisor_FAQ.py" class="button">Go to FAQ</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Card 2: Compatibility Assessment
with col2:
    st.markdown(
        """
        <div class="card">
            <h3>Compatibility Assessment</h3>
            <p>Analyze and match students to co-op opportunities that suit their skills and interests.</p>
            <a href="/pages/Advisor_Comp.py" class="button">Start Assessment</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Card 3: Track Student Progress
with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Track Student Progress</h3>
            <p>Monitor student progress and ensure they stay on track with their co-op goals.</p>
            <a href="/pages/Advisor_Progress.py" class="button">Track Progress</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
    <div class="footer">
        Powered by <a href="/">CoOperate</a>. Designed for a seamless advising experience.
    </div>
    """,
    unsafe_allow_html=True,
)
