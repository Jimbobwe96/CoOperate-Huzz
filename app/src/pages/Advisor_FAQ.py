import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Internship Advisor - Answer Questions", page_icon="❓", layout="wide")

# Page title
st.title("Answer Student Questions")
st.write("This section allows you to address common questions students may have about internships.")

# Add example question input and response functionality
question = st.text_input("Enter the student's question:", "")
if question:
    st.write(f"Answer for the question '{question}':")
    st.text_area("Response:", "Provide your answer here...")

# Back to home button
if st.button("Home"):
    st.switch_page("pages/Advisor_Home.py") 