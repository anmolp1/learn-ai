"""
run_pipeline.py - Simple orchestrator for the weather data pipeline.

Runs ingestion, transformation, and outputs the final result.
"""

from pathlib import Path

from ingestion import ingest
from transform import clean_weather_data, add_derived_fields, aggregate_by_city

OUTPUT_DIR = Path(__file__).parent / "data" / "output"


def run():
    """Execute the full pipeline: ingest -> transform -> output."""
    # Step 1: Ingest raw data
    print("=" * 50)
    print("STEP 1: Ingestion")
    raw_data = ingest()

    # Step 2: Transform
    print("\nSTEP 2: Transformation")
    df = clean_weather_data(raw_data)
    print(f"  Cleaned {len(df)} records.")

    df = add_derived_fields(df)
    print(f"  Added derived fields: temp_category, feels_like_diff.")

    summary = aggregate_by_city(df)
    print(f"  Aggregated into {len(summary)} city summaries.")

    # Step 3: Save output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "weather_summary.csv"
    summary.to_csv(output_path, index=False)

    print(f"\nSTEP 3: Output saved to {output_path}")
    print("=" * 50)
    print("\nSummary:\n")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    run()
