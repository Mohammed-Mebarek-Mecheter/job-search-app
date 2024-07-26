# src/data/process_data.py
import pandas as pd

def process_jobs(jobs):
    if not jobs:
        return pd.DataFrame()

    jobs_df = pd.DataFrame(jobs)
    cols_to_hide = ["thumbnail", "extensions", "detected_extensions", "job_id"]
    jobs_df_filtered = jobs_df.drop(columns=cols_to_hide, errors='ignore')

    return jobs_df_filtered
