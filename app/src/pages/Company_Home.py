import streamlit as st

# Top navigation bar with Home button and logo
st.markdown("""
    <style>
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        margin-bottom: 20px;
    }
    .top-bar h1 {
        margin: 0;
        font-size: 1.5em;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }
    .top-bar .search-box {
        flex-grow: 1;
        margin: 0 20px;
    }
    .top-bar .search-box input {
        width: 100%;
        padding: 8px;
        font-size: 1em;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .top-bar .right-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .top-bar img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
    }
    </style>
    <div class="top-bar">
        <h1>CoOperate</h1>
        <div class="search-box">
            <input type="text" placeholder="Search for reviews...">
        </div>
        <div class="right-section">
            <a href="/" style="text-decoration: none;">
                <button style="padding: 6px 12px; font-size: 1em; border: 1px solid #ccc; border-radius: 5px; background-color: #fff; cursor: pointer;">Sign Out</button>
            </a>
            <img src="logo_placeholder.png" alt="Profile Icon">
        </div>
    </div>
""", unsafe_allow_html=True)

# Main content layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Company Profile")
    st.text_area("Add company details here...", height=200)
    st.button("Edit Profile")
    st.button("Delete Profile")

with col2:
    st.subheader("Statistics about Applicants")
    st.text("Add relevant statistics and visualizations here.")


