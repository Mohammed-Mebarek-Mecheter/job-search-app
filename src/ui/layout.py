# src/ui/layout.py
import streamlit as st

def sidebar():
    st.sidebar.title("Search Criteria")
    search_query = st.sidebar.text_input('Enter a job title to search for', '')
    location_query = st.sidebar.text_input('Enter a location to search for jobs', '')

    # Additional search filters
    job_type = st.sidebar.selectbox('Job Type', ['', 'Full-time', 'Part-time', 'Contract', 'Temporary', 'Internship'])
    company = st.sidebar.text_input('Company')
    salary_range = st.sidebar.text_input('Salary Range')

    return search_query, location_query, job_type, company, salary_range

def main_layout():
    st.title('Worldwide Data Jobs')
    st.write('This app displays the latest worldwide data-related job postings using SerpApi.')
    view_options = st.sidebar.radio('Select View:', ["Table", "JSON", "Map"])
    return view_options
