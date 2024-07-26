# tests/test_display.py
import unittest
import pandas as pd
from src.ui.display import display_table, display_json, display_map

class TestDisplay(unittest.TestCase):

    def setUp(self):
        # Example data for testing
        self.jobs_df = pd.DataFrame([
            {"title": "Data Scientist", "location": "New York", "description": "Job description here"},
            {"title": "Data Analyst", "location": "San Francisco", "description": "Job description here"}
        ])
        self.jobs = [
            {"title": "Data Scientist", "location": "New York", "description": "Job description here"},
            {"title": "Data Analyst", "location": "San Francisco", "description": "Job description here"}
        ]

    def test_display_table(self):
        # Since display_table uses Streamlit, we can't directly test its output.
        # We'll just ensure it runs without errors for now.
        try:
            display_table(self.jobs_df)
        except Exception as e:
            self.fail(f"display_table raised an exception: {e}")

    def test_display_json(self):
        try:
            display_json(self.jobs)
        except Exception as e:
            self.fail(f"display_json raised an exception: {e}")

    def test_display_map(self):
        try:
            display_map(self.jobs)
        except Exception as e:
            self.fail(f"display_map raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
