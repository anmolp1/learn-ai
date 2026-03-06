# Starter Weather Data Pipeline

A working data pipeline that fetches weather data from the OpenWeather API, transforms it, and outputs clean results. Designed as a hands-on starting point for learning data engineering fundamentals.

## What This Pipeline Does

1. **Ingestion** (`ingestion.py`) - Fetches current weather data from the OpenWeather API for a list of cities and saves the raw JSON response.
2. **Transformation** (`transform.py`) - Cleans the raw data, standardizes units, handles nulls, and adds derived fields like temperature categories.
3. **Orchestration** (`run_pipeline.py`) - Ties ingestion and transformation together, running each step in sequence and saving final output.

## Project Structure

```
starter-pipeline/
├── README.md
├── requirements.txt
├── ingestion.py          # Fetches raw weather data
├── transform.py          # Cleans and transforms data
├── run_pipeline.py       # Orchestrates the full pipeline
├── sample_data/
│   └── weather_response.json   # Offline fallback data
├── tests/
│   └── test_transform.py      # Unit tests for transformations
└── data/                 # Created at runtime
    ├── raw/              # Raw JSON from ingestion
    └── output/           # Final transformed CSV
```

## Getting Started

### 1. Fork or copy this directory

```bash
cp -r examples/starter-pipeline my-pipeline
cd my-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Set your OpenWeather API key

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

You can get a free API key at https://openweathermap.org/api. If you skip this step, the pipeline will automatically fall back to the sample data included in `sample_data/weather_response.json`.

### 4. Run the pipeline

```bash
python run_pipeline.py
```

Output will be saved to `data/output/weather_summary.csv`.

### 5. Run the tests

```bash
pytest tests/
```

## Offline Mode

This pipeline works without an internet connection or API key. When no `OPENWEATHER_API_KEY` environment variable is set, `ingestion.py` loads pre-recorded responses from `sample_data/weather_response.json`. This makes it safe to experiment with the transformation and orchestration logic without needing external access.

## Next Steps

- Add more cities to the `CITIES` list in `ingestion.py`
- Write additional transformations in `transform.py`
- Schedule the pipeline to run on a cron job
- Swap the CSV output for a database write
