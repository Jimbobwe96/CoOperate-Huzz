import streamlit as st

# Title and logo
st.title("CoOperate")
st.text_input("Search", key="search_bar", placeholder="Search")
st.sidebar.button("Sign In")
st.sidebar.image("logo_placeholder.png", width=50, caption="Logo")

# Layout for main content
col1, col2 = st.columns(2)

with col1:
    st.header("Company Profile")
    st.text_area("Company Details", "Add company details here...", height=200)
    st.button("Edit Profile")
    st.button("Delete Profile")

with col2:
    st.header("Statistics about Applicants")
    st.text("Add relevant statistics and visualizations here.")

# Footer or additional elements
st.text("Additional footer content here, if necessary.")
