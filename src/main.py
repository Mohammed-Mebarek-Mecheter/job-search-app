# src/main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from src.data.fetch_data import fetch_jobs
from src.data.process_data import process_jobs
from src.ui.layout import sidebar, main_layout
from src.ui.display import display_table, display_json, display_map
import src.config as config

# Set page title and layout
st.set_page_config(page_title='Worldwide Data Jobs', layout='wide')

# Get user input from sidebar
search_query, location_query, job_type, company, salary_range = sidebar()

# Fetch jobs (with caching)
@st.cache_data
def get_jobs(job_titles, location_query, job_type, company, salary_range):
    return fetch_jobs(job_titles, location_query, job_type, company, salary_range)

job_titles = {"Business Analyst", "Research Analyst", "Market Research Analyst",
              "Marketing Analyst", "Data Analyst", "Quantitative Analyst",
              "Data Specialist", "Analytics Consultant", "Business Intelligence Analyst",
              "Financial Analyst", "Credit Analyst", "Data Scientist"}

if search_query:
    job_titles = {search_query}

jobs = get_jobs(job_titles, location_query, job_type, company, salary_range)

# Get view option from sidebar
view_options = main_layout()

# Display job data
if not jobs:
    st.error("No jobs found. Please adjust your search criteria.")
else:
    jobs_df_filtered = process_jobs(jobs)

    if view_options == "Table":
        display_table(jobs_df_filtered, page_size=config.PAGE_SIZE)
    elif view_options == "JSON":
        display_json(jobs)
    elif view_options == "Map":
        display_map(jobs)

# Footer section
st.markdown(
    """
    Made with ❤️ by [Mebarek](https://www.linkedin.com/in/mohammed-mecheter/). 
    [GitHub](https://github.com/Mohammed-Mebarek-Mecheter/) | 
    [LinkedIn](https://www.linkedin.com/in/mohammed-mecheter/) | 
    [Portfolio](https://mebarek.pages.dev/)
    """
)
