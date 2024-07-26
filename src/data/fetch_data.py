# src/data/fetch_data.py
import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def fetch_jobs(job_titles, location, job_type=None, company=None, salary_range=None):
    query = " | ".join(job_titles)
    if job_type:
        query += f" {job_type}"
    if company:
        query += f" {company}"
    if salary_range:
        query += f" {salary_range}"

    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": os.getenv("API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("jobs_results", [])
