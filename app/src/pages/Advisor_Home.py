import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Co-op Advisor Portal",
    page_icon="🌟",
    layout="wide"
)

# Apply custom CSS for stunning design
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

    .signout, .profile {
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

    .signout:hover, .profile:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }

    .profile-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background-color: rgba(255, 255, 255, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 50%;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
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

# Header section with profile and signout
st.markdown(
    """
    <div class="header">
        <div class="header-title">Co-op Advisor Portal</div>
        <div class="header-buttons">
            <a href="/" target="_self" class="signout">Sign Out</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main content layout
col1, col2, col3 = st.columns(3)

# Card 1: Answer Student Questions
with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Company Aggregated Data</h3>
            <p>Check Out the Aggregated Data Of Different Companies, and Make Decisions Based in the Data!</p>
            <a href="/Advisor_Data" target="_self" class="button">Aggregated Data</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Card 2: Compatibility Assessment
with col2:
    st.markdown(
        """
        <div class="card">
            <h3>Recommend Co-ops</h3>
            <p>Pick Any of Your Students and Recommend Co-ops to Them!</p>
            <a href="Advisor_Rec" target="_self" class="button">Recommend</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>My Students</h3>
            <p>View and Manage Your Students, and Add New Students!</p>
            <a href="/Advisor_Students" target="_self" class="button">Students</a>
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
