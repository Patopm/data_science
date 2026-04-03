"""
03_exploratory_analysis.py
Performs exploratory data analysis (EDA) on the sales data retrieved from
MongoDB using Pandas and NumPy.

Outputs:
- Data quality report (missing values, duplicates, dtypes)
- Descriptive statistics: mean, median, mode for numeric and categorical cols
- A summary DataFrame printed to the console
"""

import os

import numpy as np
import pandas as pd
from pymongo import MongoClient

# ── Configuration ──────────────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "todo_ventas_en_linea"
COLLECTION_NAME = "ventas"


def load_data_from_mongodb() -> pd.DataFrame:
    """Fetch all documents from MongoDB and return as DataFrame."""
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    cursor = collection.find({}, {"_id": 0})  # exclude Mongo's _id
    df = pd.DataFrame(list(cursor))
    client.close()

    # Parse date column
    df["date"] = pd.to_datetime(df["date"])
    return df


def data_quality_report(df: pd.DataFrame) -> None:
    """Print a data quality overview."""
    print("=" * 70)
    print("DATA QUALITY REPORT")
    print("=" * 70)

    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("Column data types:")
    print(df.dtypes.to_string())

    print(f"\nDuplicate rows: {df.duplicated().sum()}")

    print("\nMissing values per column:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_df = pd.DataFrame({"missing_count": missing, "missing_pct": missing_pct})
    print(missing_df.to_string())

    # Review comments: empty strings count as "no review"
    empty_reviews = (df["review_comment"] == "").sum()
    print(
        f"\nEmpty review comments: {empty_reviews} ({empty_reviews / len(df) * 100:.1f}%)"
    )


def compute_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add calculated columns useful for analysis."""
    # Total sale amount after discount
    df["total_sale"] = np.round(
        df["unit_price"] * df["quantity"] * (1 - df["discount"]), 2
    )
    # Month and year for temporal analysis
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    return df


def descriptive_statistics(df: pd.DataFrame) -> None:
    """Compute and display mean, median, and mode for key columns."""
    print("\n" + "=" * 70)
    print("DESCRIPTIVE STATISTICS (Mean, Median, Mode)")
    print("=" * 70)

    # ── Numeric columns ───────────────────────────────────────────────
    numeric_cols = ["age", "unit_price", "quantity", "discount", "total_sale"]
    stats_rows = []

    for col in numeric_cols:
        col_mean = np.mean(df[col])
        col_median = np.median(df[col])
        mode_series = df[col].mode()
        col_mode = mode_series.iloc[0] if not mode_series.empty else np.nan
        stats_rows.append(
            {
                "column": col,
                "mean": round(col_mean, 2),
                "median": round(col_median, 2),
                "mode": col_mode,
            }
        )

    stats_df = pd.DataFrame(stats_rows).set_index("column")
    print("\n── Numeric Variables ──")
    print(stats_df.to_string())

    # ── Categorical columns ───────────────────────────────────────────
    categorical_cols = ["gender", "category", "product_name"]
    print("\n── Categorical Variables (Mode / Frequency) ──")

    for col in categorical_cols:
        mode_val = df[col].mode().iloc[0]
        mode_count = (df[col] == mode_val).sum()
        print(f"\n  {col}:")
        print(f"    Mode: {mode_val} (appears {mode_count} times)")
        print(f"    Unique values: {df[col].nunique()}")
        print("    Top 5 frequencies:")
        top5_str = df[col].value_counts().head().to_string()
        for line in top5_str.split("\n"):
            print(f"      {line}")

    # ── Summary by category ───────────────────────────────────────────
    print("\n── Sales Summary by Category ──")
    summary = (
        df.groupby("category")
        .agg(
            total_revenue=("total_sale", "sum"),
            avg_sale=("total_sale", "mean"),
            total_orders=("order_id", "count"),
            avg_quantity=("quantity", "mean"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
    )
    print(summary.to_string())

    # ── Monthly trend ─────────────────────────────────────────────────
    print("\n── Average Monthly Revenue ──")
    monthly = (
        df.groupby("month")["total_sale"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"total_sale": "avg_total_sale"})
    )
    print(monthly.to_string(index=False))


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Detect outliers using the IQR method."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\n  Outliers in '{column}': {len(outliers)} records")
    print(f"    Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    print(f"    Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
    return outliers


def main() -> None:
    """Run the full exploratory analysis pipeline."""
    # Load data from MongoDB
    print("Loading data from MongoDB...")
    df = load_data_from_mongodb()
    print(f"Loaded {len(df)} records.\n")

    # Data quality
    data_quality_report(df)

    # Derived columns
    df = compute_derived_columns(df)

    # Descriptive stats
    descriptive_statistics(df)

    # Outlier detection
    print("\n" + "=" * 70)
    print("OUTLIER DETECTION (IQR Method)")
    print("=" * 70)
    for col in ["unit_price", "total_sale", "quantity"]:
        detect_outliers_iqr(df, col)

    print("\n✅ Exploratory analysis complete.")


if __name__ == "__main__":
    main()
