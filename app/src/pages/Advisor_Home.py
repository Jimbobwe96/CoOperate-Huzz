import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Internship Advisor", page_icon="🌐", layout="wide")

# Page title
st.title("Co-op Advisor Portal")
st.write("Welcome to the Co-op Advisor! Navigate through the options below to assist students with their Co-op related needs.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Answer Student Questions", "Student Compatibility Assessment"])

if page == "Home":
    st.header("Home")
    st.write(
        "This portal is designed to assist advisors in guiding students through their internship journey."
    )
    st.write("Use the navigation bar on the left to explore different functionalities.")

elif page == "Answer Student Questions":
    st.header("Answer Student Questions")
    st.write(
        "This section allows you to address common questions students may have about internships."
    )
    # Add example question input and response functionality
    question = st.text_input("Enter the student's question:", "")
    if question:
        st.write(f"Answer for the question '{question}':")
        st.text_area("Response:", "Provide your answer here...")

elif page == "Student Compatibility Assessment":
    st.header("Student Compatibility Assessment")
    st.write(
        "Analyze and assess student compatibility with various internship opportunities."
    )
    st.write("Enter student details below:")

    # Add example compatibility form
    name = st.text_input("Student Name:")
    skills = st.text_area("List of Skills:")
    preferences = st.text_area("Internship Preferences (e.g., location, type of role):")

    if st.button("Assess Compatibility"):
        st.write(f"Assessing compatibility for {name}...")
        # Placeholder for assessment logic
        st.write("Results: Based on the provided details, the student matches well with internships in [Placeholder].")
