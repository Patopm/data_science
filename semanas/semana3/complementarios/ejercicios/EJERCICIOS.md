# Resolución de Ejercicios: Python, NumPy, Pandas y Estadística

## Ejercicios de Python Básico

### Ejercicio 1: Variables y Tipos de Datos

```python
from typing import List, Dict

# 1. Crear variables de diferentes tipos
edad: int = 25
estatura: float = 1.75
nombre: str = "T3 Chat"
es_estudiante: bool = True
hobbies: List[str] = ["programar", "leer", "ajedrez"]
config: Dict[str, str] = {"tema": "oscuro", "idioma": "es"}

# 2. Convertir tipos
string_a_int: int = int("100")
float_a_int: int = int(3.99)  # Trunca a 3
int_a_float: float = float(10)

# 3. Usar f-strings
print(f"El usuario tiene {edad} años")
```

### Ejercicio 2: Control de Flujo

```python
# 1. Determinar tipo de número
def analizar_numero(n: float) -> None:
    """Determina si un número es positivo, negativo o cero."""
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Cero")

# 2. Menú con if-elif-else
opcion: str = "2"
if opcion == "1":
    print("Iniciando...")
elif opcion == "2":
    print("Configuración")
else:
    print("Salir")

# 3. Loop for sobre lista
frutas: List[str] = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# 4. While para factorial
def calcular_factorial(n: int) -> int:
    """Calcula el factorial de un número usando un ciclo while."""
    resultado: int = 1
    contador: int = n
    while contador > 0:
        resultado *= contador
        contador -= 1
    return resultado
```

### Ejercicio 3: Funciones

```python
import math

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def calcular_promedio(numeros: List[float]) -> float:
    """Devuelve el promedio de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0.0

def obtener_extremos(numeros: List[float]) -> tuple[float, float]:
    """Encuentra el valor máximo y mínimo en una lista."""
    return max(numeros), min(numeros)
```

---

## Ejercicios de NumPy

### Ejercicio 4: Operaciones con Arrays

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# 1. Suma
suma = arr1 + arr2

# 2. Multiplicar por escalar
escalar = arr1 * 10

# 3. Estadísticas
media = np.mean(arr1)
mediana = np.median(arr1)
desviacion = np.std(arr1)

# 4. Valores únicos
unicos = np.unique(np.array([1, 2, 2, 3, 1]))

# 5. Reshape 1D a 2D
arr_2d = arr1.reshape(5, 1)
```

### Ejercicio 5: Álgebra con NumPy

```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# 1. Producto punto
punto = np.dot(v1, v2)

# 2. Producto cruz
cruz = np.cross(v1, v2)

# 3. Magnitud
mag_v1 = np.linalg.norm(v1)

# 4. Normalización
v1_norm = v1 / np.linalg.norm(v1)
```

---

## Ejercicios de Pandas

### Ejercicio 6: DataFrames Básico

```python
import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofia'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}
df = pd.DataFrame(data)

# 1. Seleccionar columna
nombres = df['nombre']

# 2. Filtrar promedio > 8.5
excelencia = df[df['promedio'] > 8.5]

# 3. Ordenar por edad
ordenado = df.sort_values(by='edad')

# 4. Agregar columna 'aprobado'
df['aprobado'] = df['promedio'] >= 7.0

# 5. Group by carrera
resumen_carrera = df.groupby('carrera')['promedio'].mean()
```

### Ejercicio 7: Manipulación de Datos

```python
# 1. Manejar faltantes
df.loc[0, 'edad'] = np.nan
df['edad'] = df['edad'].fillna(df['edad'].mean())

# 2. Eliminar duplicados
df = df.drop_duplicates()

# 3. Apply
df['nombre_mayus'] = df['nombre'].apply(lambda x: x.upper())

# 4. loc e iloc
sub_df_loc = df.loc[0:2, ['nombre', 'promedio']]
sub_df_iloc = df.iloc[0:2, 0:2]

# 5. Concatenar
df2 = pd.DataFrame({'nombre': ['Pedro'], 'edad': [25]})
df_final = pd.concat([df, df2], ignore_index=True)
```

---

## Ejercicios de Visualización

### Ejercicio 8: Matplotlib

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))

# 1. Línea
plt.plot(x, y, label='Seno', color='blue', linestyle='--')

# 2. Dispersión
plt.scatter([1, 2, 3], [4, 5, 6], color='red', label='Puntos')

# 3. Histograma
plt.hist(np.random.randn(1000), bins=30, alpha=0.5)

# 4. Barras
plt.bar(['A', 'B'], [10, 20])

# 5. Personalización
plt.title("Gráfico Combinado")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()
```

---

## Ejercicios de Estadística

### Ejercicio 10: Medidas de Tendencia Central (Manual)

| Datos | Media | Mediana | Moda |
| :--- | :--- | :--- | :--- |
| [5, 3, 8, 3, 7] | 5.2 | 5 | 3 |
| [10, 20, 30, 40] | 25.0 | 25 | No hay |
| [1, 2, 2, 3, 3, 3, 4] | 2.57 | 3 | 3 |

### Ejercicio 11: Dispersión

| Datos | Rango | Varianza (\(s^2\)) | Desviación (\(s\)) |
| :--- | :--- | :--- | :--- |
| [2, 4, 4, 4, 5, 5, 7, 9] | 7 | 4.0 | 2.0 |
| [1, 3, 5, 7, 9] | 8 | 8.0 | 2.82 |

---

## Ejercicios de Investigación

### Ejercicio 12: El Proceso de Data Science

1. **¿Qué es el ciclo CRISP-DM?**
Es el *Cross-Industry Standard Process for Data Mining*. Es una metodología estándar que describe los pasos comunes que utilizan los expertos en minería de datos para abordar problemas. Consta de 6 fases: Comprensión del negocio, Comprensión de los datos, Preparación de los datos, Modelado, Evaluación y Despliegue.

2. **Fases del proceso de ciencia de datos:**
    * **Definición del problema:** Entender qué queremos resolver.
    * **Adquisición de datos:** Recolectar datos de diversas fuentes.
    * **Limpieza/Procesamiento:** Manejar valores nulos, duplicados y errores.
    * **EDA (Análisis Exploratorio):** Descubrir patrones mediante estadísticas y gráficas.
    * **Modelado:** Aplicar algoritmos de Machine Learning.
    * **Comunicación:** Presentar hallazgos a los interesados (Storytelling).

3. **¿Qué es el MVP en ciencia de datos?**
El *Producto Mínimo Viable* es la versión más sencilla de un modelo o análisis que permite validar una hipótesis de negocio con el menor esfuerzo posible. En lugar de crear un modelo complejo de Deep Learning desde el día uno, un MVP podría ser una regresión lineal simple que demuestre que los datos tienen valor predictivo.

### Ejercicio 13: Caso de Estudio (Ejemplo: Análisis de Deserción de Clientes)

* **Preguntas:** ¿Por qué los clientes están cancelando su suscripción? ¿Podemos predecir quién se irá el próximo mes?
* **Técnicas:** Análisis de correlación entre antigüedad y quejas, visualización de uso del servicio mediante histogramas y boxplots para comparar clientes activos vs. inactivos.
* **Insights:** Se encontró que los clientes que no usaban la app móvil en los primeros 10 días tenían un 80% más de probabilidad de desertar. Esto permitió crear una campaña de bienvenida dirigida.
