# src/utils/download.py
import base64
import pandas as pd
import streamlit as st

def generate_csv_download_link(df, filename="data.csv"):
    csv_file = df.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV File</a>'
