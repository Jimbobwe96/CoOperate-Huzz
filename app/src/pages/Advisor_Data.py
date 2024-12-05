import requests
import streamlit as st
import pandas as pd

try:
    position_id = 1
    response = requests.get(f'http://api:4000/cr/coop_role/{str(position_id)}')
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON list of reviews
    else:
        st.error(f"Error fetching data from API: {response.status_code}")
        data = []
except Exception as e:
    st.write("**Important**: Could not connect to sample API, so using dummy data.")
    data = [
        {"Company": "Joe", "Role": "Joe", "Location": "MA", "Pay": 9999,
         "Required GPA": 3.0, "Culture": 3, "Satisfaction": 4,
         "Compensation": 2, "Learning": 2, "Work Life Balance": 1},
    ]

# Aggregate the data for bar chart
if data:
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    
    # Select only numeric columns for bar chart
    numeric_columns = ["Culture", "Satisfaction", "Compensation", "Learning", "Work Life Balance"]
    
    # Aggregate the data for the bar chart
    bar_chart_data = df[numeric_columns].mean().reset_index()
    bar_chart_data.columns = ["Category", "Average Rating"]
    
    # Plot the bar chart
    st.bar_chart(bar_chart_data.set_index("Category"))
else:
    st.write("No data available to display.")
