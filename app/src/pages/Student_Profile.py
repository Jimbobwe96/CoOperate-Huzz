import streamlit as st

# Page configuration
st.set_page_config(page_title="CoOperate Profile Page", layout="wide")

# Header
st.title("CoOperate")

# Top Navigation Bar
col1, col2, col3, col4 = st.columns([1, 4, 4, 1])
with col1:
    st.button("Home")
with col2:
    st.write("Search Bar")  # Placeholder for search bar
with col3:
    st.write("")  # Empty space
with col4:
    st.button("Sign out")

# Body Layout
col1, col2 = st.columns([1, 3])

# Left Column
with col1:
    st.image("https://via.placeholder.com/150", caption="User Profile", width=150)  # Placeholder for profile image
    st.write("Name")
    st.write("School")
    st.write("Major")
    st.write("Graduation Year")

# Right Column
with col2:
    col21, col22, col23 = st.columns([2, 1, 1])
    with col21:
        st.write("GPA")
    with col22:
        st.write("4.0")
    with col23:
        st.button("Edit GPA")

    st.write("---")  # Divider

    col31, col32 = st.columns([3, 1])
    with col31:
        st.write("Skills")
        st.text_area("List of skills", "Skill 1\nSkill 2\nSkill 3", height=100)
    with col32:
        st.button("Edit Skills")

    st.write("---")  # Divider

    col41, col42 = st.columns([3, 1])
    with col41:
        st.write("Previous Experiences")
        st.text_area("List of Previous Experiences", "Experience 1\nExperience 2", height=100)
    with col42:
        st.button("Edit Experiences")
