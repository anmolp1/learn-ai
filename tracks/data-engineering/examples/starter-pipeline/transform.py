"""
transform.py - Transformation functions for weather data.

Provides three stages of transformation:
  1. clean_weather_data  - extract fields and handle nulls
  2. add_derived_fields  - compute temperature categories and differences
  3. aggregate_by_city   - summarize statistics per city
"""

import pandas as pd


def clean_weather_data(raw_data: list[dict]) -> pd.DataFrame:
    """
    Extract relevant fields from raw OpenWeather JSON and return a clean DataFrame.
    Handles missing or null values with sensible defaults.
    """
    records = []
    for entry in raw_data:
        main = entry.get("main", {})
        wind = entry.get("wind", {})
        weather_list = entry.get("weather", [{}])
        weather_desc = weather_list[0].get("description") if weather_list else None

        records.append({
            "city": entry.get("name", "Unknown"),
            "country": entry.get("sys", {}).get("country"),
            "temp_celsius": main.get("temp"),
            "feels_like_celsius": main.get("feels_like"),
            "humidity_pct": main.get("humidity"),
            "pressure_hpa": main.get("pressure"),
            "wind_speed_mps": wind.get("speed"),
            "description": weather_desc,
        })

    df = pd.DataFrame(records)

    # Fill missing numeric values with NaN (explicit) and strings with "unknown"
    string_cols = ["city", "country", "description"]
    for col in string_cols:
        df[col] = df[col].fillna("unknown")

    return df


def add_derived_fields(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add computed columns:
      - temp_category: cold (<10), mild (10-20), warm (20-30), hot (>30)
      - feels_like_diff: difference between feels_like and actual temp
    """
    df = df.copy()

    # Categorize temperature
    conditions = [
        df["temp_celsius"] < 10,
        df["temp_celsius"].between(10, 20, inclusive="both"),
        df["temp_celsius"].between(20, 30, inclusive="right"),
        df["temp_celsius"] > 30,
    ]
    categories = ["cold", "mild", "warm", "hot"]
    df["temp_category"] = pd.Series(
        pd.Categorical(
            [categories[i] for i in range(len(categories))],
            categories=categories,
            ordered=True,
        )
    )
    # Use numpy select for robust assignment
    import numpy as np
    df["temp_category"] = np.select(conditions, categories, default="unknown")

    # Compute feels-like difference
    df["feels_like_diff"] = df["feels_like_celsius"] - df["temp_celsius"]

    return df


def aggregate_by_city(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate weather statistics grouped by city.
    Returns one row per city with mean temperature, humidity, and wind speed.
    """
    agg_df = (
        df.groupby("city", as_index=False)
        .agg(
            avg_temp=("temp_celsius", "mean"),
            avg_humidity=("humidity_pct", "mean"),
            avg_wind_speed=("wind_speed_mps", "mean"),
            description=("description", "first"),
            temp_category=("temp_category", "first"),
        )
    )
    # Round numeric columns for readability
    numeric_cols = ["avg_temp", "avg_humidity", "avg_wind_speed"]
    agg_df[numeric_cols] = agg_df[numeric_cols].round(2)

    return agg_df
