import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Internship Advisor - Compatibility Assessment", page_icon="📊", layout="wide")

# Create a layout with columns to place the Home button on the top right
col1, col2, col3 = st.columns([1, 8, 1])  # Adjust column widths as needed

with col3:
    if st.button("Home"):
        st.switch_page('pages/Advisor_Home.py')

# Page title
st.title("Student Compatibility Assessment")
st.write("Analyze and assess student compatibility with various internship opportunities.")

# Add example compatibility form
name = st.text_input("Student Name:")
skills = st.text_area("List of Skills:")
preferences = st.text_area("Internship Preferences (e.g., location, type of role):")

if st.button("Assess Compatibility"):
    st.write(f"Assessing compatibility for {name}...")
    # Placeholder for assessment logic
    st.write("Results: Based on the provided details, the student matches well with internships in [Placeholder].")
