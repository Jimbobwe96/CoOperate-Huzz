import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Internship Advisor - Answer Questions", 
    page_icon="❓", 
    layout="wide"
)

# Create a two-column layout with the button on the far right
col1, col2 = st.columns([9, 1])  # Adjust proportions as needed
with col2:
    if st.button('Home', 
                type='secondary', 
                use_container_width=False):
        st.switch_page('pages/Advisor_Home.py')

# Page title
st.title("Answer Student Questions")
st.write("This section allows you to address common questions students may have about internships.")

# FAQs Section
st.subheader("Frequently Asked Questions")
sample_questions = [
    "What is the process to apply for an internship?",
    "How do I prepare for my internship interview?",
    "Can I switch internships mid-way if it's not a good fit?",
    "What is the expected duration of most internships?",
    "Are internships paid or unpaid?"
]

# Display FAQs
for i, question in enumerate(sample_questions, 1):
    with st.expander(f"Q{i}: {question}"):
        st.text_area(
            label=f"Response to: {question}",
            value="Type your answer here...",
            key=f"faq_response_{i}"
        )
