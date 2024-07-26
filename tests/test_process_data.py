# tests/test_process_data.py
import unittest
import pandas as pd
from src.data.process_data import process_jobs

class TestProcessData(unittest.TestCase):

    def test_process_jobs(self):
        # Example raw job data for testing
        jobs = [
            {"title": "Data Scientist", "location": "New York", "description": "Job description here"},
            {"title": "Data Analyst", "location": "San Francisco", "description": "Job description here"}
        ]
        jobs_df = process_jobs(jobs)

        # Check if the result is a DataFrame
        self.assertIsInstance(jobs_df, pd.DataFrame)

        # Check if the DataFrame contains the expected columns
        self.assertIn("title", jobs_df.columns)
        self.assertIn("location", jobs_df.columns)
        self.assertIn("description", jobs_df.columns)

if __name__ == '__main__':
    unittest.main()
