# src/utils/geocode.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_lat_lon(location):
    try:
        response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json',
            params={'address': location, 'key': GOOGLE_MAPS_API_KEY}
        )
        response.raise_for_status()
        results = response.json().get('results')
        if results:
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
        return None, None
    except requests.RequestException as e:
        return None, None
