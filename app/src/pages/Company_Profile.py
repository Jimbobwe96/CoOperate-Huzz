import streamlit as st
import requests

# API endpoints
COMPANY_STATS_ENDPOINT = "https://api.example.com/company_stats"
REVIEWS_ENDPOINT = "https://api.example.com/reviews"

def fetch_company_stats():
    try:
        response = requests.get(COMPANY_STATS_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching company statistics: {e}")
        return None

def fetch_reviews():
    try:
        response = requests.get(REVIEWS_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching reviews: {e}")
        return []

# Streamlit Layout
st.set_page_config(page_title="Company Profile", layout="wide")

# Header
st.title("Company Profile")
st.write("Explore company statistics and reviews")

# Search Bar and Navigation
search_query = st.text_input("Search for a company", "")
st.button("Home")
st.button("Sign Out")

# Fetch Data
company_stats = fetch_company_stats()
reviews = fetch_reviews()

# Layout: Company Info Section
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="Company Logo", use_column_width=True)  # Placeholder for logo
    if company_stats:
        st.subheader(company_stats.get("name", "Company Name"))
        st.write(company_stats.get("bio", "Brief Company Bio and Statistics"))
    else:
        st.subheader("Company Name")
        st.write("Brief Company Bio and Statistics")

# Layout: Reviews Section
with col2:
    st.subheader("Reviews")
    if reviews:
        for review in reviews:
            st.text_area("", review.get("text", "Review text"), height=100, disabled=True)
    else:
        st.write("No reviews available.")