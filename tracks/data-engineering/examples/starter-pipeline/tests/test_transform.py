"""
test_transform.py - Unit tests for the transform module.
"""

import pandas as pd
import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from transform import clean_weather_data, add_derived_fields


# -- Test fixtures (inline) --------------------------------------------------

SAMPLE_RAW = [
    {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {"temp": 12.5, "feels_like": 10.1, "humidity": 82, "pressure": 1012},
        "wind": {"speed": 4.5},
        "weather": [{"description": "light rain"}],
    },
    {
        "name": "Cairo",
        "sys": {"country": "EG"},
        "main": {"temp": 34.0, "feels_like": 36.2, "humidity": 20, "pressure": 1008},
        "wind": {"speed": 2.1},
        "weather": [{"description": "clear sky"}],
    },
]

SAMPLE_WITH_NULLS = [
    {
        "name": "Mystery City",
        "sys": {},
        "main": {"temp": None, "feels_like": None, "humidity": 50},
        "wind": {},
        "weather": [],
    },
]


# -- Tests --------------------------------------------------------------------

def test_clean_weather_data():
    """clean_weather_data should extract the right fields from raw JSON."""
    df = clean_weather_data(SAMPLE_RAW)

    assert len(df) == 2
    assert list(df.columns) == [
        "city", "country", "temp_celsius", "feels_like_celsius",
        "humidity_pct", "pressure_hpa", "wind_speed_mps", "description",
    ]
    assert df.iloc[0]["city"] == "London"
    assert df.iloc[0]["temp_celsius"] == 12.5
    assert df.iloc[1]["description"] == "clear sky"


def test_add_derived_fields():
    """add_derived_fields should assign correct temperature categories."""
    df = clean_weather_data(SAMPLE_RAW)
    df = add_derived_fields(df)

    assert "temp_category" in df.columns
    assert "feels_like_diff" in df.columns

    london = df[df["city"] == "London"].iloc[0]
    assert london["temp_category"] == "mild"  # 12.5 C is mild

    cairo = df[df["city"] == "Cairo"].iloc[0]
    assert cairo["temp_category"] == "hot"  # 34.0 C is hot
    assert cairo["feels_like_diff"] == pytest.approx(2.2)


def test_null_handling():
    """clean_weather_data should handle missing/null values gracefully."""
    df = clean_weather_data(SAMPLE_WITH_NULLS)

    assert len(df) == 1
    assert df.iloc[0]["city"] == "Mystery City"
    assert df.iloc[0]["country"] == "unknown"
    assert df.iloc[0]["description"] == "unknown"
    assert pd.isna(df.iloc[0]["temp_celsius"])
    assert pd.isna(df.iloc[0]["wind_speed_mps"])
