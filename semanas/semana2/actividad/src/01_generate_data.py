"""
01_generate_data.py
Generates a synthetic sales dataset with 5,000+ records and 12 columns
for "Todo ventas en Línea, S.A. de C.V."

Column types:
- Numeric (int):    age, quantity
- Numeric (float):  unit_price, discount
- Categorical:      gender, category, product_name
- Structured:       order_id, date
- Unstructured:     customer_name, customer_email, review_comment
"""

import os
import random

import numpy as np
import pandas as pd
from faker import Faker

# ── Configuration ──────────────────────────────────────────────────────
NUM_RECORDS = 5_000
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ventas.csv")
SEED = 42

# Reproducibility
random.seed(SEED)
np.random.seed(SEED)
fake = Faker("es_MX")
Faker.seed(SEED)

# ── Product catalog ───────────────────────────────────────────────────
CATALOG: dict[str, list[tuple[str, float, float]]] = {
    "Electrónica": [
        ("Smartphone Galaxy S24", 12_999.00, 18_999.00),
        ("Laptop HP Pavilion 15", 14_500.00, 22_000.00),
        ("Audífonos Bluetooth Sony", 899.00, 2_500.00),
        ("Tablet Samsung A9", 4_500.00, 7_999.00),
        ("Smartwatch Xiaomi Band 8", 699.00, 1_299.00),
    ],
    "Ropa y Moda": [
        ("Playera algodón básica", 149.00, 399.00),
        ("Jeans slim fit", 499.00, 1_200.00),
        ("Tenis deportivos Nike", 1_299.00, 2_800.00),
        ("Chamarra impermeable", 799.00, 1_800.00),
        ("Vestido casual", 350.00, 999.00),
    ],
    "Hogar y Cocina": [
        ("Licuadora Oster", 699.00, 1_500.00),
        ("Juego de sábanas Queen", 450.00, 1_200.00),
        ("Sartén antiadherente T-Fal", 349.00, 799.00),
        ("Aspiradora robot iRobot", 5_999.00, 12_000.00),
        ("Cafetera Nespresso", 2_500.00, 4_500.00),
    ],
    "Deportes": [
        ("Balón de fútbol Adidas", 399.00, 899.00),
        ("Yoga mat premium", 299.00, 699.00),
        ("Mancuernas ajustables 20kg", 1_200.00, 2_800.00),
        ("Bicicleta de montaña R29", 5_500.00, 12_000.00),
        ("Cuerda para saltar", 99.00, 299.00),
    ],
    "Libros y Educación": [
        ("Python para Ciencia de Datos", 350.00, 650.00),
        ("El Principito — edición especial", 199.00, 450.00),
        ("Curso online de inglés (código)", 999.00, 2_500.00),
        ("Enciclopedia ilustrada", 550.00, 1_200.00),
        ("Planner anual 2026", 150.00, 399.00),
    ],
}

CATEGORIES = list(CATALOG.keys())
GENDERS = ["Masculino", "Femenino", "No binario"]

# Templates for review comments (unstructured text)
REVIEW_TEMPLATES = [
    "Excelente producto, lo recomiendo ampliamente.",
    "Llegó a tiempo y en buen estado. Muy satisfecho.",
    "La calidad es regular, esperaba algo mejor por el precio.",
    "No cumplió mis expectativas, el material es muy frágil.",
    "Increíble relación calidad-precio, volvería a comprar.",
    "El envío tardó más de lo esperado pero el producto está bien.",
    "Muy buen producto. Mi familia está encantada.",
    "Pésimo servicio al cliente, pero el producto funciona.",
    "Es justo lo que necesitaba para mi día a día.",
    "Buena compra, aunque el empaque llegó un poco dañado.",
    "Supera las expectativas. Definitivamente 5 estrellas.",
    "Producto promedio, nada del otro mundo.",
    "Me encantó el diseño y la funcionalidad.",
    "Tuve problemas con la entrega pero se resolvió rápido.",
    "Lo compré como regalo y quedó perfecto.",
]


def generate_dataset() -> pd.DataFrame:
    """Generate the full synthetic dataset."""
    records: list[dict] = []

    for i in range(1, NUM_RECORDS + 1):
        # Structured: order ID and date
        order_id = f"ORD-{i:06d}"
        order_date = fake.date_between(start_date="-3y", end_date="today").isoformat()

        # Unstructured: customer info
        customer_name = fake.name()
        customer_email = fake.email()

        # Numeric (int): age
        age = int(np.random.normal(loc=35, scale=12))
        age = max(18, min(age, 75))  # clamp between 18 and 75

        # Categorical: gender
        gender = random.choices(GENDERS, weights=[0.45, 0.45, 0.10], k=1)[0]

        # Categorical: category and product
        category = random.choice(CATEGORIES)
        product_name, price_min, price_max = random.choice(CATALOG[category])

        # Numeric (float): unit price with some variance
        unit_price = round(random.uniform(price_min, price_max), 2)

        # Numeric (int): quantity — most purchases are small
        quantity = int(np.random.exponential(scale=2)) + 1
        quantity = min(quantity, 20)

        # Numeric (float): discount percentage (0% - 30%)
        # 60% of the time there is no discount
        if random.random() < 0.6:
            discount = 0.0
        else:
            discount = round(random.uniform(0.05, 0.30), 2)

        # Unstructured: review comment (only ~70% leave a review)
        if random.random() < 0.7:
            review_comment = random.choice(REVIEW_TEMPLATES)
        else:
            review_comment = ""

        records.append(
            {
                "order_id": order_id,
                "date": order_date,
                "customer_name": customer_name,
                "customer_email": customer_email,
                "age": age,
                "gender": gender,
                "category": category,
                "product_name": product_name,
                "unit_price": unit_price,
                "quantity": quantity,
                "discount": discount,
                "review_comment": review_comment,
            }
        )

    df = pd.DataFrame(records)
    return df


def main() -> None:
    """Entry point: generate and save dataset."""
    print("Generating synthetic sales dataset...")
    df = generate_dataset()

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print(f"Dataset saved to {OUTPUT_FILE}")
    print(f"Shape: {df.shape}")
    print(f"\nColumn types:\n{df.dtypes}")
    print(f"\nFirst 5 rows:\n{df.head()}")


if __name__ == "__main__":
    main()
