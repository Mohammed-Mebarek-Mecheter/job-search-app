import streamlit as st
import pandas as pd
from serpapi import GoogleSearch
import psycopg2
import pydeck as pdk
import geocoder
import base64
import os

# Import API key from config file
from config import SERPAPI_API_KEY

# Database connection
conn = psycopg2.connect(database="job_db", user="postgres", password="mebarek", host="localhost")
cursor = conn.cursor()

# Set page title and layout
st.set_page_config(page_title='Data Jobs in Qatar', layout='wide')

# Display title and introduction
st.title('Data-Related Jobs in Qatar')
st.write('This app displays the latest data-related job postings in Qatar using SerpApi.')

# User input for job search
search_query = st.sidebar.text_input('Enter a job title to search for', '')

job_titles = {"Business Analyst", "Research Analyst", "Market Research Analyst",
              "Marketing Analyst", "Data Analyst", "Quantitative Analyst",
              "Data Specialist", "Analytics Consultant", "Business Intelligence Analyst",
              "Financial Analyst", "Credit Analyst", "Data Scientist"}

if search_query:
    job_titles = {search_query}

params = {
    "engine": "google_jobs",
    "q": " | ".join(job_titles),
    "location": "Qatar",
    "api_key": os.getenv("API_KEY")
}

search = GoogleSearch(params)
results = search.get_dict()

# Display job data in a table
jobs = results.get("jobs_results", [])

if not jobs:
    st.error('Search to find your Data Dream Job')
else:
    # Display job data in tabs
    with st.sidebar.expander("View Options"):
        tab_selected = st.radio('Select View:', ["Table", "JSON", "Map"])

    if tab_selected == "Table":
        jobs_df = pd.DataFrame(jobs)
        # Remove unwanted columns temporarily
        cols_to_hide = ["thumbnail", "extensions", "detected_extensions", "job_id"]
        jobs_df_filtered = jobs_df.drop(columns=cols_to_hide, errors='ignore')

        # Display download link for CSV file
        csv_file = jobs_df_filtered.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()
        st.markdown(f'<a href="data:file/csv;base64,{b64}" download="job_results.csv">Download CSV File</a>', unsafe_allow_html=True)

        st.table(jobs_df_filtered)
    elif tab_selected == "JSON":
        st.json(results)
    elif tab_selected == "Map":
        # Extract latitude and longitude from job locations
        job_locations = [job["location"] for job in jobs if job.get("location")]
        job_latitudes = []
        job_longitudes = []
        for location in job_locations:
            try:
                lat, lon = geocoder.google(location).latlng
                job_latitudes.append(lat)
                job_longitudes.append(lon)
            except:
                pass

        # Create a Pydeck scatterplot layer
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=pd.DataFrame({"lat": job_latitudes, "lon": job_longitudes}),
            get_position=["lon", "lat"],
            radius_scale=100,
            radius_min_pixels=3,
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True,
        )

        # Set the initial view state
        view_state = pdk.ViewState(latitude=25.2854, longitude=51.5310, zoom=7, bearing=0, pitch=0)

        # Create the Pydeck map
        map_ = pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=view_state,
            layers=[layer],
        )

        # Render the map in Streamlit
        st.pydeck_chart(map_)

# Footer section
st.markdown(
    """
    Made with ❤️ by [Mebarek](https://www.linkedin.com/in/mohammed-mecheter/). 
    [GitHub](https://github.com/Mohammed-Mebarek-Mecheter/) | 
    [LinkedIn](https://www.linkedin.com/in/mohammed-mecheter/) | 
    [Portfolio](https://mebarek.pages.dev/)
    """
)
