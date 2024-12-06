import streamlit as st

st.set_page_config(
    page_title="Company Dashboard",
    page_icon="🌟",
    layout="wide"
)

st.markdown(
    """
    <style>
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

    .signout {
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

    .signout:hover {
        background-color: rgba(255, 255, 255, 0.4);
        transform: scale(1.05);
    }

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

st.markdown(
    """
    <div class="header">
        <div class="header-title">Company Dashboard</div>
        <div class="header-buttons">
            <a href="/" target="_self" class="signout">Sign Out</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Company Profile</h3>
            <p>View and Edit Your Company Information</p>
            <a href="/Company_Profile" target="_self" class="button">Profile</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>Job Postings</h3>
            <p>Manage and Review Your Company Job Postings</p>
            <a href="/Job_Postings" target="_self" class="button">Postings</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Add Co-op</h3>
            <p>Add New Co-op Positions for Students</p>
            <a href="/Add_Job" target="_self" class="button">Add</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="footer">
        Powered by <a href="/">CoOperate</a>. Designed for a seamless company experience.
    </div>
    """,
    unsafe_allow_html=True,
)
