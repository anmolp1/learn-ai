# Pre-Selected Data Sources

This document provides three ready-to-use data sources for your pipeline projects. Each one includes everything you need to get started — no research required.

---

## 1. OpenWeather API (Live API - Weather Data)

**What it provides:** Current weather and forecast data for any city in the world.

**Free tier:** 1,000 API calls per day (more than enough for this program).

### Sign-Up

1. Go to [openweathermap.org/api](https://openweathermap.org/api).
2. Click **Sign Up** and create a free account.
3. After email verification, go to **API Keys** in your account dashboard.
4. Copy your API key. It may take up to 2 hours to activate after creation.

### Endpoint

```
GET https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
```

### Sample Response

```json
{
  "coord": {"lon": -122.42, "lat": 37.77},
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "main": {
    "temp": 18.5,
    "feels_like": 17.2,
    "temp_min": 15.0,
    "temp_max": 21.0,
    "pressure": 1013,
    "humidity": 65
  },
  "wind": {"speed": 3.6, "deg": 270},
  "dt": 1700000000,
  "name": "San Francisco"
}
```

### Starter Code

See the full working pipeline in `examples/starter-pipeline/` which demonstrates extraction, transformation, and loading using the OpenWeather API as its data source.

### Useful fields for pipeline projects

| Field | Path | Type |
|-------|------|------|
| City name | `name` | string |
| Temperature (C) | `main.temp` | float |
| Humidity (%) | `main.humidity` | int |
| Weather description | `weather[0].description` | string |
| Wind speed (m/s) | `wind.speed` | float |
| Timestamp | `dt` | Unix timestamp |

---

## 2. GitHub API (Live API - No Auth Required)

**What it provides:** Repository metadata, commit history, issues, and more for any public repository.

**Free tier (unauthenticated):** 60 requests per hour. No sign-up needed.

### Endpoint

```
GET https://api.github.com/repos/{owner}/{repo}
```

### Sample Response (for `pandas-dev/pandas`)

```json
{
  "id": 8514,
  "name": "pandas",
  "full_name": "pandas-dev/pandas",
  "description": "Flexible and powerful data analysis / manipulation library for Python",
  "stargazers_count": 43000,
  "forks_count": 17500,
  "open_issues_count": 3500,
  "language": "Python",
  "created_at": "2010-08-24T01:37:33Z",
  "updated_at": "2025-01-15T12:00:00Z",
  "subscribers_count": 1200,
  "license": {"key": "bsd-3-clause", "name": "BSD 3-Clause"}
}
```

### Starter Code Snippet

```python
import requests
import pandas as pd

def fetch_github_repos(topic: str, per_page: int = 30) -> pd.DataFrame:
    """
    Fetch public repositories for a given topic from the GitHub API.

    Args:
        topic: Search topic (e.g., "data-engineering", "machine-learning").
        per_page: Number of results per page (max 100).

    Returns:
        DataFrame with repository metadata.
    """
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"topic:{topic}",
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    repos = response.json()["items"]
    records = [
        {
            "name": r["full_name"],
            "stars": r["stargazers_count"],
            "forks": r["forks_count"],
            "open_issues": r["open_issues_count"],
            "language": r["language"],
            "created_at": r["created_at"],
            "description": r["description"]
        }
        for r in repos
    ]
    return pd.DataFrame(records)


if __name__ == "__main__":
    df = fetch_github_repos("data-engineering")
    print(df.head())
    print(f"\nFetched {len(df)} repositories.")
```

### Other useful endpoints (no auth)

| Endpoint | Description |
|----------|-------------|
| `GET /repos/{owner}/{repo}/commits` | Recent commits |
| `GET /repos/{owner}/{repo}/issues` | Open issues |
| `GET /repos/{owner}/{repo}/languages` | Language breakdown |
| `GET /users/{username}/repos` | All public repos for a user |

---

## 3. Provided CSV (Local File - No Setup)

**What it provides:** E-commerce transaction data, ready for immediate use in pipeline exercises.

**File location:** `examples/ecommerce_transactions.csv`

**No sign-up, no API key, no rate limits.** This is the fastest way to start building.

### Description

The CSV contains simulated e-commerce transaction records with fields suitable for practicing common data engineering tasks: deduplication, data type casting, aggregation, and quality checks.

### Expected columns

| Column | Type | Description |
|--------|------|-------------|
| transaction_id | string | Unique transaction identifier |
| customer_id | string | Customer identifier |
| product_name | string | Name of the purchased product |
| category | string | Product category |
| quantity | int | Number of units purchased |
| unit_price | float | Price per unit |
| transaction_date | string | Date of purchase (YYYY-MM-DD) |
| payment_method | string | Payment type (credit_card, debit_card, paypal, etc.) |

### Quick start

```python
import pandas as pd

df = pd.read_csv("examples/ecommerce_transactions.csv")
print(df.info())
print(df.head())
```

---

## Which Source Should I Pick?

| If you want... | Use |
|----------------|-----|
| The simplest start (no setup) | Provided CSV |
| To practice API extraction | OpenWeather API |
| To skip API key sign-up | GitHub API |
| A richer pipeline project | Combine two sources (e.g., GitHub repos + weather for contributor locations) |
