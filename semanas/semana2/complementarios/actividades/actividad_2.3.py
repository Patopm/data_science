"""
Actividad 2.3: Operaciones CRUD en MongoDB

Requisitos:
    pip install pymongo
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from datetime import datetime
import sys


# ---------------------------------------------------------------------------
# CONFIGURACIÓN DE CONEXIÓN
# ---------------------------------------------------------------------------

MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "empresa"
COLLECTION_NAME = "empleados"


# ---------------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------------


def separador(titulo: str) -> None:
    """Imprime un separador visual con un título para mejor legibilidad."""
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def mostrar_empleado(empleado: dict) -> None:
    """
    Muestra un documento de empleado con formato legible.

    Args:
        empleado (dict): Documento de empleado retornado por MongoDB.
    """
    print(
        f"  | ID: {empleado['_id']}\n"
        f"  | Nombre:       {empleado['nombre']}\n"
        f"  | Departamento: {empleado['departamento']}\n"
        f"  | Salario:      ${empleado['salario']:,.2f}\n"
        f"  | Activo:       {'Sí' if empleado.get('activo') else 'No'}\n"
        f"  | Fecha Alta:   {empleado.get('fecha_alta', 'N/A')}\n" + "-" * 50
    )


# ---------------------------------------------------------------------------
# CONEXIÓN A MONGODB
# ---------------------------------------------------------------------------


def conectar() -> tuple:
    """
    Establece la conexión con MongoDB.

    Returns:
        tuple: (cliente, colección) si la conexión es exitosa.

    Raises:
        SystemExit: Si no se puede conectar al servidor.
    """
    try:
        cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        # Verificar que el servidor responde
        cliente.admin.command("ping")
        db = cliente[DATABASE_NAME]
        coleccion = db[COLLECTION_NAME]
        print(f"Conexión exitosa a MongoDB → Base de datos: '{DATABASE_NAME}'")
        return cliente, coleccion

    except ConnectionFailure:
        print("Error: No se pudo conectar a MongoDB.")
        print("Asegúrate de que el servidor esté corriendo en:", MONGO_URI)
        sys.exit(1)


# ---------------------------------------------------------------------------
# CREATE — Insertar documentos
# ---------------------------------------------------------------------------


def insertar_empleados(coleccion) -> None:
    """
    Inserta 10 documentos de empleados en la colección.
    Si la colección ya tiene datos, la limpia antes de insertar.

    Args:
        coleccion: Objeto de colección de pymongo.
    """
    separador("CREATE — Insertar Empleados")

    # Limpiar colección para evitar duplicados al re-ejecutar el script
    coleccion.drop()
    print("Colección limpiada para inserción fresca.\n")

    fecha_hoy = datetime.now()

    empleados = [
        {
            "nombre": "Ana García",
            "departamento": "Tecnología",
            "salario": 55000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Carlos López",
            "departamento": "Tecnología",
            "salario": 62000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "María Hernández",
            "departamento": "Recursos Humanos",
            "salario": 48000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "José Martínez",
            "departamento": "Ventas",
            "salario": 45000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Laura Sánchez",
            "departamento": "Finanzas",
            "salario": 70000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Pedro Ramírez",
            "departamento": "Tecnología",
            "salario": 58000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Sofía Torres",
            "departamento": "Ventas",
            "salario": 43000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Diego Flores",
            "departamento": "Finanzas",
            "salario": 67000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Valentina Ruiz",
            "departamento": "Recursos Humanos",
            "salario": 51000.00,
            "activo": True,
            "fecha_alta": fecha_hoy,
        },
        {
            "nombre": "Andrés Morales",
            "departamento": "Ventas",
            "salario": 46500.00,
            "activo": False,
            "fecha_alta": fecha_hoy,
        },
    ]

    resultado = coleccion.insert_many(empleados)

    print(f"Se insertaron {len(resultado.inserted_ids)} empleados correctamente.")
    print("IDs generados:")
    for i, _id in enumerate(resultado.inserted_ids, 1):
        print(f"   {i:>2}. {_id}")


# ---------------------------------------------------------------------------
# READ — Consultar documentos
# ---------------------------------------------------------------------------


def leer_empleados(coleccion) -> None:
    """
    Realiza distintas consultas de lectura sobre la colección.

    Consultas incluidas:
        - Todos los empleados
        - Empleados de un departamento específico
        - Empleados con salario mayor a un monto
        - Empleados activos ordenados por salario

    Args:
        coleccion: Objeto de colección de pymongo.
    """
    separador("READ — Consultar Empleados")

    # -- Consulta 1: Todos los empleados --
    print("\nTodos los empleados:\n" + "-" * 50)
    for emp in coleccion.find():
        mostrar_empleado(emp)

    # -- Consulta 2: Filtrar por departamento --
    departamento_filtro = "Tecnología"
    print(f"\nEmpleados del departamento: '{departamento_filtro}'\n" + "-" * 50)
    resultados = list(coleccion.find({"departamento": departamento_filtro}))

    if resultados:
        for emp in resultados:
            mostrar_empleado(emp)
        print(f"Total encontrados: {len(resultados)}")
    else:
        print("No se encontraron empleados en ese departamento.")

    # -- Consulta 3: Salario mayor a un valor --
    salario_minimo = 60000
    print(f"\nEmpleados con salario > ${salario_minimo:,}\n" + "-" * 50)
    for emp in coleccion.find(
        {"salario": {"$gt": salario_minimo}},
        sort=[("salario", -1)],  # Ordenar de mayor a menor
    ):
        mostrar_empleado(emp)

    # -- Consulta 4: Contar por departamento (aggregation) --
    print("\nTotal de empleados por departamento:\n" + "-" * 50)
    pipeline = [
        {"$group": {"_id": "$departamento", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
    ]
    for doc in coleccion.aggregate(pipeline):
        print(f"{doc['_id']:<25} → {doc['total']} empleado(s)")


# ---------------------------------------------------------------------------
# UPDATE — Actualizar documentos
# ---------------------------------------------------------------------------


def actualizar_empleados(coleccion) -> None:
    """
    Realiza operaciones de actualización en la colección.

    Operaciones incluidas:
        - Actualizar el salario de un empleado específico (update_one)
        - Aplicar aumento general a un departamento (update_many)

    Args:
        coleccion: Objeto de colección de pymongo.
    """
    separador("UPDATE — Actualizar Empleados")

    # -- Actualización 1: Salario de un empleado específico --
    nombre_objetivo = "Ana García"
    nuevo_salario = 65000.00

    print(f"\nActualizando salario de '{nombre_objetivo}'...")

    antes = coleccion.find_one({"nombre": nombre_objetivo})
    print(f"Salario antes: ${antes['salario']:,.2f}")

    resultado = coleccion.update_one(
        {"nombre": nombre_objetivo}, {"$set": {"salario": nuevo_salario}}
    )

    despues = coleccion.find_one({"nombre": nombre_objetivo})
    print(f"Salario después: ${despues['salario']:,.2f}")
    print(f"Documentos modificados: {resultado.modified_count}")

    # -- Actualización 2: Aumento del 10 % a todo un departamento --
    depto_aumento = "Ventas"
    porcentaje = 1.10  # 10 % de aumento

    print(f"\nAplicando 10% de aumento al departamento '{depto_aumento}'...")

    resultado_many = coleccion.update_many(
        {"departamento": depto_aumento},
        {"$mul": {"salario": porcentaje}},  # $mul multiplica el campo
    )

    print(f"Documentos modificados: {resultado_many.modified_count}")
    print(f"\nSalarios actualizados en '{depto_aumento}':")
    for emp in coleccion.find({"departamento": depto_aumento}):
        print(f"- {emp['nombre']:<25} → ${emp['salario']:,.2f}")


# ---------------------------------------------------------------------------
# DELETE — Eliminar documentos
# ---------------------------------------------------------------------------


def eliminar_empleados(coleccion) -> None:
    """
    Realiza operaciones de eliminación en la colección.

    Operaciones incluidas:
        - Eliminar un empleado específico por nombre (delete_one)
        - Eliminar empleados inactivos (delete_many)

    Args:
        coleccion: Objeto de colección de pymongo.
    """
    separador("DELETE — Eliminar Empleados")

    # Mostrar total antes de eliminar
    total_antes = coleccion.count_documents({})
    print(f"\nTotal de empleados antes: {total_antes}")

    # -- Eliminación 1: Un empleado específico --
    nombre_eliminar = "Carlos López"
    print(f"\nEliminando empleado: '{nombre_eliminar}'...")

    resultado_one = coleccion.delete_one({"nombre": nombre_eliminar})
    print(f"Documentos eliminados: {resultado_one.deleted_count}")

    # -- Eliminación 2: Empleados inactivos --
    print("\nEliminando empleados inactivos (activo: False)...")
    resultado_many = coleccion.delete_many({"activo": False})
    print(f"Documentos eliminados: {resultado_many.deleted_count}")

    # Mostrar total después de eliminar
    total_despues = coleccion.count_documents({})
    print(f"\nTotal de empleados después: {total_despues}")

    # Mostrar empleados restantes
    print("\nEmpleados restantes en la colección:\n" + "-" * 50)
    for emp in coleccion.find():
        mostrar_empleado(emp)


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Función principal que orquesta todas las operaciones CRUD.
    Garantiza que la conexión a MongoDB se cierre al finalizar.
    """
    print("\nIniciando Actividad 2.3 — Operaciones CRUD en MongoDB")
    print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    cliente, coleccion = conectar()

    try:
        insertar_empleados(coleccion)  # CREATE
        leer_empleados(coleccion)  # READ
        actualizar_empleados(coleccion)  # UPDATE
        eliminar_empleados(coleccion)  # DELETE

        separador("Operaciones CRUD completadas exitosamente ✅")

    except OperationFailure as e:
        print(f"\nError de operación en MongoDB: {e}")

    finally:
        cliente.close()
        print("\nConexión a MongoDB cerrada.\n")


if __name__ == "__main__":
    main()
