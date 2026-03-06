# Session 1: Practice Scenarios

Work through these three scenarios to practice using AI for real data engineering tasks. Each scenario is self-contained with the context, artifacts, tasks, and expected outputs you need.

---

## Scenario 1: Schema-Aware Querying

### Context

You have been given access to a BigQuery table called `analytics.orders`. Your task is to write AI prompts that generate correct SQL queries based on the table schema. The goal is to practice giving AI enough context (the schema) to produce accurate, runnable queries on the first try.

### Artifact: Table Schema

```
Table: analytics.orders

Column Name      | Type      | Description
-----------------|-----------|--------------------------------------------
order_id         | STRING    | Unique order identifier (e.g., "ORD-00001")
customer_id      | STRING    | Customer identifier (e.g., "CUST-1234")
order_date       | DATE      | Date the order was placed
product_name     | STRING    | Name of the product ordered
category         | STRING    | Product category (Electronics, Clothing, Home, Food)
quantity         | INTEGER   | Number of units ordered (always >= 1)
unit_price       | FLOAT64   | Price per unit in USD
region           | STRING    | Customer region (North, South, East, West)
```

### Task

Write prompts (to use with Claude or another AI assistant) that generate SQL queries for each of the following. Include the schema in your prompt so the AI has full context.

**Query 1:** Find the top 5 customers by total spend (quantity * unit_price) in the last 90 days.

**Query 2:** Calculate the month-over-month percentage change in total revenue per category.

**Query 3:** Identify orders that are likely duplicates — same customer_id, product_name, quantity, and order_date.

### Expected Output

For each query, you should have:
- The prompt you wrote (including how you provided the schema)
- The SQL query the AI generated
- A brief check: does the SQL reference the correct column names and types from the schema?

**Example of a good prompt structure:**

```
Given this BigQuery table schema:

Table: analytics.orders
- order_id (STRING): unique order identifier
- customer_id (STRING): customer identifier
- order_date (DATE): date the order was placed
- product_name (STRING): product name
- category (STRING): one of Electronics, Clothing, Home, Food
- quantity (INTEGER): units ordered, always >= 1
- unit_price (FLOAT64): price per unit in USD
- region (STRING): one of North, South, East, West

Write a BigQuery SQL query to [your specific request here].
```

---

## Scenario 2: Debug a Broken Script

### Context

A colleague wrote a Python ETL script that extracts order data from a CSV, transforms it, and loads a summary into a new CSV. The script runs without syntax errors but produces incorrect results. There are 3 bugs hidden in the code. Your task is to use AI to find and fix all three.

### Artifact: The Broken Script

```python
import pandas as pd
from datetime import datetime

def extract(file_path: str) -> pd.DataFrame:
    """Load order data from CSV."""
    df = pd.read_csv(file_path)
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and aggregate order data."""
    # Filter to only orders from January 2025
    df["order_date"] = pd.to_datetime(df["order_date"])
    jan_orders = df[
        (df["order_date"] >= "2025-01-01") & (df["order_date"] < "2025-01-31")
    ]

    # Calculate total revenue per order
    jan_orders = jan_orders.copy()
    jan_orders["total_revenue"] = jan_orders["quantity"] * jan_orders["unit_cost"]

    # Aggregate by category
    summary = jan_orders.groupby("category").agg(
        total_orders=("order_id", "count"),
        total_revenue=("total_revenue", "sum"),
        avg_quantity=("quantity", "mean")
    ).reset_index()

    return summary

def load(df: pd.DataFrame, output_path: str) -> None:
    """Save summary to CSV."""
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

def run_pipeline():
    raw_data = extract("orders.csv")
    summary = transform(raw_data)
    load(summary, "january_summary.csv")

if __name__ == "__main__":
    run_pipeline()
```

### Task

1. Copy the script above into a prompt for your AI assistant.
2. Ask it to identify all bugs in the script.
3. For each bug found, document:
   - What the bug is
   - Why it causes incorrect results
   - The fix

### Expected Output

The AI should identify these three bugs:

**Bug 1 — Wrong column name (line with `unit_cost`):**
The script references `unit_cost` but the standard column name is `unit_price`. This will cause a `KeyError` at runtime.
Fix: Change `jan_orders["unit_cost"]` to `jan_orders["unit_price"]`.

**Bug 2 — Missing null handling:**
The script does not handle rows where `quantity` or `unit_price` might be null/NaN. If any nulls exist, the `total_revenue` calculation will propagate NaN, and the aggregated `total_revenue` sum will be incorrect (or NaN).
Fix: Add `jan_orders = jan_orders.dropna(subset=["quantity", "unit_price"])` before the revenue calculation, or use `fillna(0)` depending on business requirements.

**Bug 3 — Off-by-one in date filter:**
The filter uses `< "2025-01-31"`, which excludes January 31st. To include all of January, it should be `< "2025-02-01"`.
Fix: Change `"2025-01-31"` to `"2025-02-01"`.

---

## Scenario 3: Clean a Messy CSV

### Context

You have a CSV file with real-world data quality problems. Your task is to use AI to write a Python cleaning script. The CSV is provided at `examples/sample_sales.csv` in this repository.

### Artifact

The file `examples/sample_sales.csv` contains 50 rows of sales data with the following columns:

```
date, product, region, units_sold, revenue, cost
```

Known data quality issues:
- **Inconsistent region casing:** The `region` column has values like "East", "EAST", "east", "WEST", "west", etc.
- **Zero revenue rows:** Several rows have `revenue = 0` even though `units_sold > 0`, which is likely a data entry error.
- **Missing costs:** Some rows have empty/missing values in the `cost` column.

### Task

1. Open the CSV and examine it (or describe the issues above to your AI assistant).
2. Ask the AI to write a Python script that:
   - Loads the CSV
   - Standardizes the `region` column to title case (e.g., "East", "West", "North", "South")
   - Flags or imputes rows where `revenue = 0` but `units_sold > 0` (e.g., estimate revenue using the average revenue-per-unit for that product)
   - Handles missing `cost` values (e.g., fill with the median cost for that product, or flag for review)
   - Adds a `profit_margin` column calculated as `(revenue - cost) / revenue`
   - Saves the cleaned data to a new CSV

3. Run the script on `examples/sample_sales.csv` and verify the output.

### Expected Output

A Python script that produces a cleaned CSV with:
- All region values in title case (exactly "East", "West", "North", "South")
- No zero-revenue rows (either corrected or flagged)
- No missing cost values (either filled or flagged)
- A new `profit_margin` column with values between 0 and 1 for valid rows
- A brief printed summary of what was cleaned (e.g., "Standardized 12 region values, imputed 3 zero-revenue rows, filled 3 missing costs")

**Example output summary:**

```
Loaded 50 rows from sample_sales.csv
Standardized 12 region values to title case
Imputed revenue for 3 rows using product average
Filled 3 missing cost values using product median
Added profit_margin column
Saved cleaned data to sample_sales_cleaned.csv (50 rows)
```
