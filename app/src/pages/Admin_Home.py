import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Admin Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Admin Dashboard")
page = st.sidebar.radio("Navigation", ["Home", "Aggregated Scores", "Flagged Reviews"])

# Home page
if page == "Home":
    st.title("Welcome to the Admin Dashboard")
    st.write("Use the sidebar to navigate to different sections.")
    st.image("admin_dashboard_placeholder.png", caption="Admin Dashboard", use_column_width=True)

# Aggregated Scores Page
elif page == "Aggregated Scores":
    st.title("Aggregated Scores for Companies")
    st.write("Select a company to view its aggregated score.")
    
    # Example list of company links (can be generated dynamically)
    companies = ["Company A", "Company B", "Company C", "Company D"]
    for company in companies:
        st.markdown(f"- [View scores for {company}](#)")

# Flagged Reviews Page
elif page == "Flagged Reviews":
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

