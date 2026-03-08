# Capstone Data Sources

This document provides API endpoints, sample responses, and starter code for each capstone project. Pick your project in [Session 0](../curriculum/session-00-prework/) and use this page as your technical reference.

> **Note:** The `examples/starter-pipeline/` directory uses the OpenWeather API as a teaching example. It's a useful reference for ingestion patterns but uses a different data source than the capstone projects below.

---

## 1. USGS Earthquake API (Earthquake Monitor)

**What it provides:** Real-time and historical earthquake event data worldwide.

**Free tier:** Unlimited. No API key required.

### Endpoints

```
# All earthquakes in the past hour (GeoJSON)
GET https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

# All earthquakes in the past day
GET https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson

# Query with filters (date range, magnitude, location)
GET https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2024-01-01&minmagnitude=4
```

### Sample Response

```json
{
  "type": "FeatureCollection",
  "metadata": {
    "generated": 1700000000000,
    "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
    "title": "USGS All Earthquakes, Past Hour",
    "count": 12
  },
  "features": [
    {
      "type": "Feature",
      "properties": {
        "mag": 4.2,
        "place": "15 km NNE of Ridgecrest, CA",
        "time": 1700000000000,
        "type": "earthquake",
        "title": "M 4.2 - 15 km NNE of Ridgecrest, CA",
        "tsunami": 0,
        "felt": 25,
        "alert": "green"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-117.6135, 35.7038, 5.2]
      }
    }
  ]
}
```

### Starter Code Snippet

```python
import requests
import pandas as pd

def fetch_earthquakes(period: str = "day", min_magnitude: float = 0) -> pd.DataFrame:
    """
    Fetch earthquake events from USGS GeoJSON feed.

    Args:
        period: "hour", "day", "week", or "month".
        min_magnitude: Minimum magnitude filter (applied client-side for feed endpoints).

    Returns:
        DataFrame with earthquake event data.
    """
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{period}.geojson"
    response = requests.get(url)
    response.raise_for_status()

    features = response.json()["features"]
    records = [
        {
            "id": f["id"],
            "magnitude": f["properties"]["mag"],
            "place": f["properties"]["place"],
            "time": pd.to_datetime(f["properties"]["time"], unit="ms"),
            "longitude": f["geometry"]["coordinates"][0],
            "latitude": f["geometry"]["coordinates"][1],
            "depth_km": f["geometry"]["coordinates"][2],
            "felt": f["properties"].get("felt"),
            "alert": f["properties"].get("alert"),
        }
        for f in features
        if f["properties"]["mag"] is not None and f["properties"]["mag"] >= min_magnitude
    ]
    return pd.DataFrame(records)


if __name__ == "__main__":
    df = fetch_earthquakes("day", min_magnitude=2.5)
    print(df.head())
    print(f"\nFetched {len(df)} earthquakes (M2.5+) in the past day.")
```

### Useful fields

| Field | Path | Type |
|-------|------|------|
| Magnitude | `properties.mag` | float |
| Location description | `properties.place` | string |
| Event time (ms) | `properties.time` | Unix timestamp (ms) |
| Longitude | `geometry.coordinates[0]` | float |
| Latitude | `geometry.coordinates[1]` | float |
| Depth (km) | `geometry.coordinates[2]` | float |
| Felt reports | `properties.felt` | int or null |
| Alert level | `properties.alert` | string or null |

---

## 2. NYC Open Data — 311 Service Requests (NYC 311 Complaint Analyzer)

**What it provides:** All 311 service requests filed in New York City since 2010. 30M+ records.

**Free tier:** Unlimited with a free app token (recommended to avoid throttling). Register at [NYC Open Data](https://data.cityofnewyork.us/profile/edit/developer_settings).

### Endpoint

```
# Recent complaints (SODA API), most recent 1000
GET https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=1000&$order=created_date DESC

# With date filter
GET https://data.cityofnewyork.us/resource/erm2-nwe9.json?$where=created_date > '2024-01-01'&$limit=5000

# With app token (recommended)
GET https://data.cityofnewyork.us/resource/erm2-nwe9.json?$$app_token=YOUR_TOKEN&$limit=1000
```

### Sample Response

```json
[
  {
    "unique_key": "62345678",
    "created_date": "2024-11-15T14:30:00.000",
    "closed_date": "2024-11-16T09:15:00.000",
    "agency": "NYPD",
    "agency_name": "New York City Police Department",
    "complaint_type": "Noise - Residential",
    "descriptor": "Loud Music/Party",
    "location_type": "Residential Building/House",
    "incident_zip": "10001",
    "city": "NEW YORK",
    "borough": "MANHATTAN",
    "latitude": "40.7484",
    "longitude": "-73.9967",
    "status": "Closed",
    "community_board": "05 MANHATTAN",
    "resolution_description": "The Police Department responded to the complaint."
  }
]
```

### Starter Code Snippet

```python
import requests
import pandas as pd

def fetch_311_complaints(days_back: int = 7, limit: int = 5000, app_token: str = None) -> pd.DataFrame:
    """
    Fetch recent NYC 311 service requests via SODA API.

    Args:
        days_back: Number of days to look back.
        limit: Max rows to return (API max per request is 50,000).
        app_token: NYC Open Data app token (optional but recommended).

    Returns:
        DataFrame with complaint records.
    """
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    cutoff = (pd.Timestamp.now() - pd.Timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%S")
    params = {
        "$where": f"created_date > '{cutoff}'",
        "$limit": limit,
        "$order": "created_date DESC",
    }
    if app_token:
        params["$$app_token"] = app_token

    response = requests.get(url, params=params)
    response.raise_for_status()

    return pd.DataFrame(response.json())


if __name__ == "__main__":
    df = fetch_311_complaints(days_back=7, limit=1000)
    print(df[["created_date", "complaint_type", "borough", "status"]].head(10))
    print(f"\nFetched {len(df)} complaints from the past week.")
```

### Useful fields

| Field | Path | Type |
|-------|------|------|
| Complaint type | `complaint_type` | string (~200 categories) |
| Descriptor | `descriptor` | string (sub-category) |
| Borough | `borough` | string |
| Created date | `created_date` | ISO timestamp |
| Closed date | `closed_date` | ISO timestamp or null |
| Status | `status` | string (Open/Closed/Pending) |
| Community board | `community_board` | string |
| Zip code | `incident_zip` | string |

---

## 3. GitHub Events API (GitHub Activity Tracker)

**What it provides:** Public event activity (pushes, PRs, issues, reviews, etc.) for any GitHub repository.

**Free tier:** 5,000 requests/hour with a personal access token. 60/hour without auth.

### Setup

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Select scope: `public_repo` (read-only access to public repos is sufficient)
4. Copy the token and set it as an environment variable: `export GITHUB_TOKEN=ghp_...`

### Endpoints

```
# Events for a specific repo (most recent 100, paginated)
GET https://api.github.com/repos/{owner}/{repo}/events?per_page=100

# Public events (all of GitHub — high volume)
GET https://api.github.com/events?per_page=100
```

### Sample Response

```json
[
  {
    "id": "12345678901",
    "type": "PushEvent",
    "actor": {
      "login": "octocat",
      "display_login": "octocat"
    },
    "repo": {
      "name": "pandas-dev/pandas"
    },
    "payload": {
      "push_id": 999999,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "commits": [
        {
          "sha": "abc123",
          "message": "Fix null handling in groupby"
        }
      ]
    },
    "created_at": "2024-11-15T14:30:00Z"
  }
]
```

### Starter Code Snippet

```python
import requests
import pandas as pd

def fetch_repo_events(owner: str, repo: str, token: str = None, pages: int = 3) -> pd.DataFrame:
    """
    Fetch recent events for a GitHub repository.

    Args:
        owner: Repository owner (e.g., "pandas-dev").
        repo: Repository name (e.g., "pandas").
        token: GitHub personal access token (optional but recommended).
        pages: Number of pages to fetch (100 events per page, max 3 pages = 300 events).

    Returns:
        DataFrame with event data.
    """
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    all_events = []
    for page in range(1, pages + 1):
        url = f"https://api.github.com/repos/{owner}/{repo}/events"
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        response.raise_for_status()
        events = response.json()
        if not events:
            break
        all_events.extend(events)

    records = [
        {
            "id": e["id"],
            "type": e["type"],
            "actor": e["actor"]["login"],
            "repo": e["repo"]["name"],
            "created_at": pd.to_datetime(e["created_at"]),
        }
        for e in all_events
    ]
    return pd.DataFrame(records)


if __name__ == "__main__":
    df = fetch_repo_events("pandas-dev", "pandas")
    print(df.head(10))
    print(f"\nFetched {len(df)} events.")
    print(f"Event types: {df['type'].value_counts().to_dict()}")
```

### Event types

| Event Type | Description |
|-----------|-------------|
| `PushEvent` | Commits pushed to a branch |
| `PullRequestEvent` | PR opened, closed, merged, or edited |
| `IssuesEvent` | Issue opened, closed, or edited |
| `PullRequestReviewEvent` | PR review submitted |
| `CreateEvent` | Branch or tag created |
| `DeleteEvent` | Branch or tag deleted |
| `ForkEvent` | Repository forked |
| `WatchEvent` | Repository starred |
| `IssueCommentEvent` | Comment on an issue or PR |
| `ReleaseEvent` | Release published |

---

## 4. Open-Meteo API (Weather Analytics)

**What it provides:** Weather forecasts (up to 16 days) and historical weather data (80+ years) for any location. 60+ weather variables.

**Free tier:** Unlimited for non-commercial use. No API key required.

### Endpoints

```
# Hourly forecast for a location (next 7 days)
GET https://api.open-meteo.com/v1/forecast?latitude=37.77&longitude=-122.42&hourly=temperature_2m,precipitation,wind_speed_10m

# Historical weather (actuals)
GET https://archive-api.open-meteo.com/v1/archive?latitude=37.77&longitude=-122.42&start_date=2024-01-01&end_date=2024-01-31&hourly=temperature_2m,precipitation

# Daily aggregates (simpler)
GET https://api.open-meteo.com/v1/forecast?latitude=37.77&longitude=-122.42&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto
```

### Sample Response

```json
{
  "latitude": 37.775,
  "longitude": -122.4194,
  "timezone": "America/Los_Angeles",
  "hourly_units": {
    "time": "iso8601",
    "temperature_2m": "\u00b0C",
    "precipitation": "mm",
    "wind_speed_10m": "km/h"
  },
  "hourly": {
    "time": [
      "2024-11-15T00:00",
      "2024-11-15T01:00",
      "2024-11-15T02:00"
    ],
    "temperature_2m": [12.3, 11.8, 11.2],
    "precipitation": [0.0, 0.0, 0.1],
    "wind_speed_10m": [8.5, 7.2, 6.8]
  }
}
```

### Starter Code Snippet

```python
import requests
import pandas as pd

def fetch_weather(lat: float, lon: float, city_name: str = "Unknown") -> pd.DataFrame:
    """
    Fetch hourly weather forecast from Open-Meteo.

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.
        city_name: Label for the location (for the output DataFrame).

    Returns:
        DataFrame with hourly weather data.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,wind_speed_10m,relative_humidity_2m",
        "timezone": "auto",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame({
        "time": pd.to_datetime(data["hourly"]["time"]),
        "temperature_c": data["hourly"]["temperature_2m"],
        "precipitation_mm": data["hourly"]["precipitation"],
        "wind_speed_kmh": data["hourly"]["wind_speed_10m"],
        "humidity_pct": data["hourly"]["relative_humidity_2m"],
    })
    df["city"] = city_name
    return df


if __name__ == "__main__":
    cities = [
        ("San Francisco", 37.77, -122.42),
        ("New York", 40.71, -74.01),
        ("Chicago", 41.88, -87.63),
    ]
    frames = [fetch_weather(lat, lon, name) for name, lat, lon in cities]
    df = pd.concat(frames, ignore_index=True)
    print(df.head(10))
    print(f"\nFetched {len(df)} hourly records across {len(cities)} cities.")
```

### Useful variables

| Variable | Endpoint param | Unit |
|----------|---------------|------|
| Temperature | `temperature_2m` | °C |
| Precipitation | `precipitation` | mm |
| Wind speed | `wind_speed_10m` | km/h |
| Humidity | `relative_humidity_2m` | % |
| Cloud cover | `cloud_cover` | % |
| Pressure | `surface_pressure` | hPa |
| UV index | `uv_index` | index |

See the [Open-Meteo docs](https://open-meteo.com/en/docs) for the full list of 60+ available variables.

---

## Which Source Should I Pick?

All four projects are designed to exercise the full rubric equally. Pick based on the **problem domain** that interests you most:

| If you like... | Pick |
|----------------|------|
| Geoscience, real-time events, geographic analysis | Earthquake Monitor |
| Civic data, NLP/classification, large datasets | NYC 311 Complaint Analyzer |
| Tech/open-source, event streams, contributor analytics | GitHub Activity Tracker |
| Weather, time-series, forecast accuracy analysis | Weather Analytics |

See the [capstone guidelines](../capstone/guidelines.md) for full project details including pipeline stages, AI integration points, and session milestones.
