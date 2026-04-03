"""
04_visualizations.py
Creates three key visualizations from the sales dataset:
1. Box plot       — distribution of total_sale by category
2. Scatter plot   — unit_price vs. quantity colored by category
3. Histogram      — distribution of total_sale

All charts are saved to the visualizations/ directory.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pymongo import MongoClient

# ── Configuration ──────────────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "todo_ventas_en_linea"
COLLECTION_NAME = "ventas"
VIZ_DIR = os.path.join(os.path.dirname(__file__), "..", "visualizations")

# Seaborn style
sns.set_theme(style="whitegrid", palette="Set2", font_scale=1.1)


def load_data() -> pd.DataFrame:
    """Fetch data from MongoDB and prepare it."""
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    cursor = collection.find({}, {"_id": 0})
    df = pd.DataFrame(list(cursor))
    client.close()

    df["date"] = pd.to_datetime(df["date"])
    df["total_sale"] = np.round(
        df["unit_price"] * df["quantity"] * (1 - df["discount"]), 2
    )
    return df


def create_boxplot(df: pd.DataFrame) -> None:
    """
    Box plot: distribution of total_sale per product category.
    Useful to identify medians, spread, and outliers per category.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(
        data=df,
        x="category",
        y="total_sale",
        hue="category",
        legend=False,
        ax=ax,
    )
    ax.set_title(
        "Distribución del Monto Total de Venta por Categoría",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Categoría de Producto")
    ax.set_ylabel("Monto Total de Venta (MXN)")
    ax.tick_params(axis="x", rotation=15)
    fig.tight_layout()

    path = os.path.join(VIZ_DIR, "boxplot_ventas.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Box plot saved to {path}")


def create_scatter(df: pd.DataFrame) -> None:
    """
    Scatter plot: unit_price vs quantity, colored by category.
    Shows the relationship between price and purchase volume.
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.scatterplot(
        data=df,
        x="unit_price",
        y="quantity",
        hue="category",
        alpha=0.6,
        edgecolor="none",
        s=40,
        ax=ax,
    )
    ax.set_title(
        "Relación entre Precio Unitario y Cantidad Comprada",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Precio Unitario (MXN)")
    ax.set_ylabel("Cantidad Comprada")
    ax.legend(title="Categoría", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()

    path = os.path.join(VIZ_DIR, "scatter_precio_cantidad.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Scatter plot saved to {path}")


def create_histogram(df: pd.DataFrame) -> None:
    """
    Histogram: distribution of total_sale amounts.
    Reveals the frequency of different sale ranges.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(
        data=df,
        x="total_sale",
        bins=60,
        kde=True,
        color="steelblue",
        edgecolor="white",
        ax=ax,
    )
    ax.set_title(
        "Distribución de los Montos Totales de Venta",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Monto Total de Venta (MXN)")
    ax.set_ylabel("Frecuencia")

    # Add vertical lines for mean and median
    mean_val = df["total_sale"].mean()
    median_val = df["total_sale"].median()
    ax.axvline(
        mean_val, color="red", linestyle="--", linewidth=1.5,
        label=f"Media: ${mean_val:,.0f}",
    )
    ax.axvline(
        median_val, color="orange", linestyle="-.", linewidth=1.5,
        label=f"Mediana: ${median_val:,.0f}",
    )
    ax.legend()
    fig.tight_layout()

    path = os.path.join(VIZ_DIR, "histograma_total.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Histogram saved to {path}")


def main() -> None:
    """Generate all visualizations."""
    os.makedirs(VIZ_DIR, exist_ok=True)

    print("Loading data from MongoDB...")
    df = load_data()
    print(f"Loaded {len(df)} records.\n")

    create_boxplot(df)
    create_scatter(df)
    create_histogram(df)

    print("\n✅ All visualizations generated successfully.")


if __name__ == "__main__":
    main()

