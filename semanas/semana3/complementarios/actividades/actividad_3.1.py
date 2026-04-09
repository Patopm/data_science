"""
Actividad 3.1: Refuerzo de Python para Análisis de Datos
Este script demuestra conceptos clave de Python y resuelve 5 ejercicios básicos.
"""

import pandas as pd

# ==========================================
# PARTE 1: DEMOSTRACIÓN DE CONCEPTOS
# ==========================================


def demostracion_conceptos():
    """
    Demuestra el uso de listas, diccionarios, DataFrames de Pandas,
    funciones lambda, list comprehensions y manejo de errores.
    """
    print("--- 1. Listas, Diccionarios y DataFrames ---")

    # Lista
    nombres = ["Ana", "Carlos", "Beatriz", "David"]
    edades = [28, 34, 25, 42]

    # Diccionario
    datos_diccionario = {
        "Nombre": nombres,
        "Edad": edades,
        "Ciudad": ["Madrid", "Bogotá", "Lima", "CDMX"],
    }

    # DataFrame
    df = pd.DataFrame(datos_diccionario)
    print("DataFrame creado:")
    print(df)

    print("\n--- 2. List Comprehensions ---")
    # Crear una nueva lista con las edades en 5 años usando list comprehension
    edades_futuras = [edad + 5 for edad in edades]
    print(f"Edades actuales: {edades}\nEdades en 5 años: {edades_futuras}")

    print("\n--- 3. Funciones Lambda ---")
    # Usar lambda para filtrar edades mayores a 30
    mayores_de_30 = list(filter(lambda x: x > 30, edades))
    print(f"Edades mayores a 30: {mayores_de_30}")

    print("\n--- 4. Manejo de Errores ---")
    try:
        # Intentar acceder a una columna que no existe
        _columna_inexistente = df["Salario"]
    except KeyError as e:
        print(f"Error capturado: La columna {e} no existe en el DataFrame.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Bloque 'finally' ejecutado: El manejo de errores ha terminado.")


# ==========================================
# PARTE 2: 5 EJERCICIOS DE PROGRAMACIÓN BÁSICA
# ==========================================


def ejercicio_1_sumar_pares(numeros):
    """
    Ejercicio 1: Calcula la suma de todos los números pares en una lista.

    Args:
        numeros (list): Lista de números enteros.

    Returns:
        int: La suma de los números pares.
    """
    return sum([num for num in numeros if num % 2 == 0])


def ejercicio_2_es_palindromo(texto):
    """
    Ejercicio 2: Verifica si una cadena de texto es un palíndromo.

    Args:
        texto (str): La cadena a evaluar.

    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    texto_limpio = str(texto).replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]


def ejercicio_3_factorial(n):
    """
    Ejercicio 3: Calcula el factorial de un número usando recursividad.

    Args:
        n (int): Número entero positivo.

    Returns:
        int: El factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    return n * ejercicio_3_factorial(n - 1)


def ejercicio_4_contar_vocales(texto):
    """
    Ejercicio 4: Cuenta el número de vocales en una cadena de texto.

    Args:
        texto (str): El texto a analizar.

    Returns:
        int: Cantidad total de vocales.
    """
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for char in texto if char in vocales)


def ejercicio_5_fibonacci(limite):
    """
    Ejercicio 5: Genera la secuencia de Fibonacci hasta una cantidad dada de términos.

    Args:
        limite (int): Cantidad de números de la secuencia a generar.

    Returns:
        list: Lista con la secuencia de Fibonacci.
    """
    if limite <= 0:
        return []
    elif limite == 1:
        return [0]

    secuencia = [0, 1]
    while len(secuencia) < limite:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia


# ==========================================
# EJECUCIÓN DEL SCRIPT
# ==========================================

if __name__ == "__main__":
    # Ejecutar demostración
    demostracion_conceptos()

    print("\n==========================================")
    print("RESULTADOS DE LOS EJERCICIOS")
    print("==========================================\n")

    # Prueba Ejercicio 1
    lista_num = [1, 2, 3, 4, 5, 6]
    print(f"Ej 1 - Suma de pares en {lista_num}: {ejercicio_1_sumar_pares(lista_num)}")

    # Prueba Ejercicio 2
    frase = "Anita lava la tina"
    print(f"Ej 2 - ¿'{frase}' es palíndromo?: {ejercicio_2_es_palindromo(frase)}")

    # Prueba Ejercicio 3
    num_fact = 5
    print(f"Ej 3 - Factorial de {num_fact}: {ejercicio_3_factorial(num_fact)}")

    # Prueba Ejercicio 4
    texto_vocales = "Hola Mundo desde Python"
    print(
        f"Ej 4 - Vocales en '{texto_vocales}': {ejercicio_4_contar_vocales(texto_vocales)}"
    )

    # Prueba Ejercicio 5
    terminos_fibo = 8
    print(
        f"Ej 5 - Primeros {terminos_fibo} términos de Fibonacci: {ejercicio_5_fibonacci(terminos_fibo)}"
    )
