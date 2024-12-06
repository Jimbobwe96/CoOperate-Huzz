import requests
import streamlit as st
import pandas as pd
import plotly.express as px

try:
    position_id = 1
    response = requests.get('http://api:4000/c/company/positions/agg_data')
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
    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Get unique companies
    company_options = df['Company'].unique().tolist()

    # Default selection: First 5 companies or any arbitrary selection
    default_selection = company_options[:5]  # Select the first 5 companies

    # Multiselect for filtering
    selected_companies = st.multiselect(
        "Select Companies:",
        options=company_options,
        default=default_selection  # Default to first 5 companies
    )

    # Filter data based on the selected companies
    filtered_df = df[df['Company'].isin(selected_companies)]

    # Plot grouped bar chart for the selected companies
    fig = px.bar(
        filtered_df,
        x='Company',
        y='avg_overall_score',
        color='PosTitle',
        barmode='group',
        title="Average Overall Scores by Company and CoopRole",
        labels={'avg_overall_score': 'Average Overall Score', 'PosTitle': 'CoopRole'}
    )

    fig.update_traces(width=0.5)  # Adjust the bar width (default is usually smaller)

    # Customize the layout
    fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Average Overall Score",
        legend_title="CoopRole",
        xaxis_tickangle=-45,
        width=1200,
        height=700
    )

    # Display chart in Streamlit
    st.plotly_chart(fig)

    # Display filtered table for additional clarity (optional)
    st.write("Filtered Table Representation")
    st.dataframe(filtered_df)
