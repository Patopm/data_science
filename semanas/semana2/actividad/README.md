# Actividad 2 — Análisis Exploratorio de Datos de Ventas

## Descripción del Proyecto

Proyecto de ciencia de datos que analiza un conjunto de datos de ventas de la
tienda en línea **"Todo ventas en Línea, S.A. de C.V."** El objetivo es
realizar un análisis exploratorio para comprender el rendimiento de las ventas
y extraer información valiosa para la toma de decisiones comerciales.

## Definición del Problema

### Objetivo

Analizar los datos de ventas de los últimos años para identificar patrones de
consumo, productos más rentables, segmentos de mercado clave y temporalidades
de mayor demanda, con el fin de fundamentar las estrategias comerciales de la
organización para el presente año.

### Preguntas Clave de Investigación

1. **¿Cuáles son los productos y categorías con mayor volumen de ventas e
   ingresos?**
2. **¿Qué segmentos de clientes (edad, género, región) generan más valor?**
3. **¿En qué meses o épocas del año se concentran las ventas más altas?**
4. **¿Cuál es la relación entre el precio del producto, la cantidad vendida y
   el descuento aplicado?**
5. **¿Existen valores atípicos en los montos de venta que requieran atención
   especial?**

## Tecnologías Utilizadas

- **Python 3.11+** con UV como gestor de paquetes
- **MongoDB** como base de datos NoSQL
- **Pandas / NumPy** para manipulación y análisis de datos
- **Matplotlib / Seaborn** para visualización
- **Faker** para generación de datos sintéticos

## Estructura del Proyecto

```text
├── README.md               # Este archivo
├── data/
│   └── ventas.csv          # Dataset generado (5,000+ registros)
├── visualizations/
│   ├── boxplot_ventas.png
│   ├── scatter_precio_cantidad.png
│   └── histograma_total.png
├── src/
│   ├── 01_generate_data.py       # Generación de datos aleatorios
│   ├── 02_load_to_mongodb.py     # Carga de datos a MongoDB
│   ├── 03_exploratory_analysis.py # Análisis exploratorio con Pandas/NumPy
│   └── 04_visualizations.py      # Creación de gráficas
└── docs/
    └── analysis_report.md  # Reporte de interpretación de resultados
```

## Instalación y Ejecución

### Prerrequisitos

- Python 3.11 o superior
- [UV](https://docs.astral.sh/uv/) instalado
- MongoDB corriendo localmente en `localhost:27017`

### Pasos

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd actividad-2-ciencia-datos

# 2. Instalar dependencias con UV
uv sync

# 3. Ejecutar los scripts en orden
uv run python src/01_generate_data.py
uv run python src/02_load_to_mongodb.py
uv run python src/03_exploratory_analysis.py
uv run python src/04_visualizations.py
```

## Descripción del Dataset

El dataset contiene **5,000 registros** con las siguientes **12 columnas**:

| Columna | Tipo | Descripción |
| ---- | --- | ---- |
| `order_id` | Estructurado | Identificador único del pedido |
| `date` | Estructurado | Fecha de la transacción (YYYY-MM-DD) |
| `customer_name` | No estructurado | Nombre completo del cliente |
| `customer_email` | No estructurado | Correo electrónico del cliente |
| `age` | Numérico (int) | Edad del cliente |
| `gender` | Categórico | Género del cliente |
| `category` | Categórico | Categoría del producto |
| `product_name` | Categórico | Nombre del producto |
| `unit_price` | Numérico (dec) | Precio unitario del producto |
| `quantity` | Numérico (int) | Cantidad de unidades compradas |
| `discount` | Numérico (dec) | Porcentaje de descuento aplicado |
| `review_comment` | No estructurado | Comentario de reseña del cliente |

Adicionalmente se calculan columnas derivadas como `total_sale` durante
el análisis.
