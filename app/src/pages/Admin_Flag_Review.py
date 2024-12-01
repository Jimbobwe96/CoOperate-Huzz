import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard - Flagged Reviews", layout="wide")

st.title("Review Flagged Reviews")
st.write("Here are reviews flagged by users or the system.")

# Example flagged reviews
flagged_reviews = [
    {"id": 1, "review": "This product is terrible!", "flag_reason": "Inappropriate language"},
    {"id": 2, "review": "Best service ever, but too expensive!", "flag_reason": "Suspicious activity"},
    {"id": 3, "review": "I hate this company.", "flag_reason": "Negative sentiment"},
]

for review in flagged_reviews:
    st.subheader(f"Review ID: {review['id']}")
    st.write(f"**Review:** {review['review']}")
    st.write(f"**Reason for flagging:** {review['flag_reason']}")
    st.button("Approve", key=f"approve_{review['id']}")
    st.button("Reject", key=f"reject_{review['id']}")

# Navigation buttons
if st.button("Home"):
    st.switch_page("pages/Admin_Home.py")