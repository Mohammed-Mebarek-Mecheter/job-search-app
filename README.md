# JobSearcher App

## Overview

This Streamlit app displays the latest worldwide data-related job postings using the SerpApi to fetch real-time job data based on user-defined search criteria.

![JobSearcher App](app.PNG)

## Features

- Search for data-related jobs worldwide.
- View job listings in a table format with pagination.
- Download job listings as a CSV file.
- View job listings on a map (if location data is available).
- View job listings in JSON format.
- Filter job listings by job type, company, and salary range.

## Installation

To run the JobSearcher app locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Mohammed-Mebarek-Mecheter/job-search-app.git
```

2. Navigate to the project directory:

```bash
cd job-search-app
```

3. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory of the project and add your SerpApi API key:

```env
API_KEY=your_serpapi_api_key
```

6. Run the Streamlit app:

```bash
streamlit run src/main.py
```

## Usage

- Upon running the app, users will be presented with a search interface.
- Enter desired job titles and search parameters in the sidebar, then click the "Search" button.
- The app will fetch job listings from the Google Jobs API based on the provided criteria.
- Users can view detailed information about each job listing and filter results as needed.
- To download search results, click on the "Download CSV" link.
- View job listings in a table format with pagination.
- View job listings on a map if location data is available.
- View job listings in JSON format.

## Project Structure

```
JobSearcherApp/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── fetch_data.py
│   │   ├── process_data.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── layout.py
│   │   ├── display.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── geocode.py
│   │   ├── download.py
│   ├── config.py
│   ├── main.py
└── tests/
    ├── __init__.py
    ├── test_fetch_data.py
    ├── test_process_data.py
    ├── test_display.py
```

## Contributing

Contributions to the JobSearcher app are welcome! If you have any suggestions, bug fixes, or feature requests, please open an issue or submit a pull request on GitHub.

## Author

- LinkedIn: [Let's connect](https://www.linkedin.com/in/mohammed-mecheter/)
- Portfolio: [Mebarek](https://mebarek.pages.dev/)
