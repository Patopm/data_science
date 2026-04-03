"""
02_load_to_mongodb.py
Loads the generated CSV dataset into a MongoDB collection.

Database:  todo_ventas_en_linea
Collection: ventas
"""

import os

import pandas as pd
from pymongo import MongoClient

# ── Configuration ──────────────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "todo_ventas_en_linea"
COLLECTION_NAME = "ventas"
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ventas.csv")


def load_csv_to_mongodb() -> None:
    """Read the CSV file and insert all records into MongoDB."""
    # Read CSV
    print(f"Reading CSV from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    print(f"Loaded {len(df)} records with {len(df.columns)} columns.")

    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Drop existing collection to avoid duplicates on re-runs
    collection.drop()
    print(f"Collection '{COLLECTION_NAME}' cleared.")

    # Convert DataFrame to list of dicts and insert
    records = df.to_dict(orient="records")
    result = collection.insert_many(records)
    print(
        f"Inserted {len(result.inserted_ids)} documents "
        f"into '{DB_NAME}.{COLLECTION_NAME}'."
    )

    # ── Quick verification ─────────────────────────────────────────────
    print(f"\nTotal documents in collection: {collection.count_documents({})}")
    print("\nSample document:")
    sample = collection.find_one()
    if sample:
        sample.pop("_id", None)
        for key, value in sample.items():
            print(f"  {key}: {value}")

    client.close()
    print("\nMongoDB connection closed.")


if __name__ == "__main__":
    load_csv_to_mongodb()
