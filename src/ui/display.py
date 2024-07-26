# src/ui/display.py
import streamlit as st
import base64
import pydeck as pdk
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

def display_table(jobs_df, page_size=10):
    # Implement pagination
    total_pages = (len(jobs_df) // page_size) + 1
    page = st.sidebar.number_input('Page', min_value=1, max_value=total_pages, value=1)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    # Display table with pagination
    st.table(jobs_df.iloc[start_idx:end_idx])

    # Generate CSV download link
    csv_file = jobs_df.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    st.markdown(f'<a href="data:file/csv;base64,{b64}" download="job_results.csv">Download CSV File</a>', unsafe_allow_html=True)

def display_json(jobs):
    st.json(jobs)

def display_map(jobs):
    # Extract locations
    job_locations = [job.get("location", "") for job in jobs if job.get("location")]

    if not job_locations:
        st.error("No valid job locations found.")
        return

    # Initialize geocoder
    geolocator = Nominatim(user_agent="job_search_app")

    # Geocode locations
    geocoded_locations = []
    for location in job_locations:
        try:
            location_info = geolocator.geocode(location)
            if location_info:
                geocoded_locations.append({
                    "name": location,
                    "lat": location_info.latitude,
                    "lon": location_info.longitude
                })
            else:
                st.warning(f"Couldn't find coordinates for location: {location}")
        except (GeocoderTimedOut, GeocoderUnavailable):
            st.warning(f"Geocoding service timed out for location: {location}")

    # Create a DataFrame from geocoded locations
    df = pd.DataFrame(geocoded_locations)

    if df.empty:
        st.error("No valid locations to display on the map.")
        return

    # Calculate the center of the map
    center_lat = df['lat'].mean()
    center_lon = df['lon'].mean()

    # Create the map
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=center_lat,
            longitude=center_lon,
            zoom=3,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=100000,
                pickable=True,
                auto_highlight=True
            ),
        ],
        tooltip={
            "html": "<b>{name}</b>",
            "style": {
                "backgroundColor": "steelblue",
                "color": "white"
            }
        }
    ))

    # Display the data table below the map
    st.write(df)
