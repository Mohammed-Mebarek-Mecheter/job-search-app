# tests/test_fetch_data.py
import unittest
from src.data.fetch_data import fetch_jobs

class TestFetchData(unittest.TestCase):

    def test_fetch_jobs(self):
        # Example job titles and location for testing
        job_titles = ["Data Scientist"]
        location = "New York"
        jobs = fetch_jobs(job_titles, location)

        # Check if the jobs list is not empty
        self.assertIsInstance(jobs, list)
        if jobs:
            self.assertIsInstance(jobs[0], dict)

if __name__ == '__main__':
    unittest.main()
