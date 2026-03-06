"""
ingestion.py - Fetches current weather data from the OpenWeather API.

If no API key is set, falls back to sample_data/weather_response.json
so the pipeline can run offline.
"""

import json
import os
from pathlib import Path

import requests

# Cities to fetch weather data for
CITIES = ["London", "New York", "Tokyo", "Sydney", "Cairo"]

API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
SAMPLE_DATA_PATH = Path(__file__).parent / "sample_data" / "weather_response.json"
RAW_OUTPUT_DIR = Path(__file__).parent / "data" / "raw"


def fetch_weather(cities: list[str], api_key: str) -> list[dict]:
    """Fetch current weather for each city from the OpenWeather API."""
    results = []
    for city in cities:
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        results.append(response.json())
    return results


def load_sample_data() -> list[dict]:
    """Load pre-recorded weather data from the sample file."""
    with open(SAMPLE_DATA_PATH, "r") as f:
        return json.load(f)


def save_raw_data(data: list[dict]) -> Path:
    """Save raw JSON data to the data/raw/ directory."""
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_OUTPUT_DIR / "weather_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    return output_path


def ingest() -> list[dict]:
    """Run the ingestion step. Uses API if key is available, otherwise sample data."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if api_key:
        print(f"Fetching live weather data for {len(CITIES)} cities...")
        data = fetch_weather(CITIES, api_key)
    else:
        print("No API key found. Loading sample data for offline mode.")
        data = load_sample_data()

    output_path = save_raw_data(data)
    print(f"Raw data saved to {output_path}")
    return data


if __name__ == "__main__":
    ingest()
