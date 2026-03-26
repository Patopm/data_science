# Resolución de Ejercicios Complementarios - Semana 2

## Ejercicios de Bases de Datos SQL

### Ejercicio 1: Consultas Básicas

Dada la siguiente tabla `empleados`:

| id | nombre     | departamento | salario |
| -- | ---------- | ------------ | ------- |
| 1  | Juan       | IT           | 50000   |
| 2  | María      | HR           | 45000   |
| 3  | Carlos     | IT           | 55000   |
| 4  | Ana        | Finanzas     | 48000   |
| 5  | Pedro      | Marketing    | 42000   |

Consultas SQL para:

1. Seleccionar todos los empleados

```sql
SELECT * FROM empleados;
```

1. Seleccionar nombres y salarios de empleados de IT

```sql
SELECT nombre, salario
FROM empleados
WHERE departamento = 'IT';
```

1. Encontrar el empleado con mayor salario

```sql
SELECT *
FROM empleados
WHERE salario = (SELECT MAX(salario) FROM empleados);
```

1. Contar empleados por departamento

```sql
SELECT departamento, COUNT(*)
FROM empleados
GROUP BY departamento;
```

1. Actualizar el salario de María a 50000

```sql
UPDATE empleados
SET salario = 50000
WHERE nombre = 'María';
```

### Ejercicio 2: Joins

Dadas las tablas:

**empleados**

| id | nombre   | id_departamento |
| -- | -------- | ---------------- |
| 1  | Juan     | 1                |
| 2  | María    | 2                |
| 3  | Carlos   | 1                |

**departamentos**

| id | nombre      |
| -- | ----------- |
| 1  | IT          |
| 2  | HR          |
| 3  | Finanzas    |

Consultas para:

1. INNER JOIN entre empleados y departamentos

```sql
SELECT *
FROM empleados AS e
INNER JOIN departamentos AS d ON e.id_departamento = d.id;
```

1. LEFT JOIN mostrando todos los empleados

```sql
SELECT *
FROM empleados AS e
LEFT JOIN departamentos AS d ON e.id_departamento = d.id;
```

1. Contar empleados por departamento

```sql
SELECT d.nombre, COUNT(e.id) AS total_empleados
FROM departamentos AS d
LEFT JOIN empleados AS e ON d.id = e.id_departamento
GROUP BY d.nombre;
```

---

## Ejercicios de JSON y Estructuras de Datos

### Ejercicio 3: Manipulación de JSON

Dado el siguiente JSON:

```json
{
  "empleados": [
    {"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
    {"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
    {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
  ]
}
```

Asumiendo que se guarda en la variable `empleados`.

1. Extraer los nombres de todos los empleados

```python
# Imprimirlos en pantalla
for e in empleados['empleados']:
    print(e['nombre'])
```

```python
# Extraerlos a una lista
list(map(lambda e: e['nombre'], empleados['empleados']))
```

1. Agregar una nueva habilidad a Juan

```python
# Con for
for e in empleados['empleados']:
    if e['nombre'] == 'Juan':
        e['habilidades'].append('nueva habilidad')
```

```python
# Con funcion
juan = next((e for e in empleados['empleados'] if e['nombre'] == 'Juan'), None)
if juan:
    juan['habilidades'].append('nueva habilidad')
```

1. Crear un nuevo empleado con id: 4

```python
empleados['empleados'].append({"id": 4, "nombre": "Erick", "habilidades": ["Ninguna"]})
```

1. Eliminar las habilidades de María

```python
# Con for
for e in empleados['empleados']:
    if e['nombre'] == 'María':
        e['habilidades'] = []
```

```python
# Con funcion
maria = next((e for e in empleados['empleados'] if e['nombre'] == 'María'), None)
if maria:
    maria['habilidades'] = []
```

### Ejercicio 4: Estructuras de Datos en Python

Implementar las siguientes estructuras:

```python
# Lista de diccionarios (simulando una tabla)
empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

# Ejercicios:
# 1. Agregar un nuevo empleado
empleados.append({"id": 4, "nombre": "Mateo", "salario": 30000})

# 2. Buscar empleado por id
id = 1 # cualquier numero
for e in empleados:
    if e['id'] == id:
      print(e)
      break
else:
    print(f'Error: no se encontro el empleado con id {id}')

# 3. Calcular promedio de salarios
sum(map(lambda e: e['salario'], empleados)) / len(empleados)

# 4. Filtrar empleados con salario > 50000
list(filter(lambda e: e['salario'] > 50000, empleados))

# 5. Actualizar el nombre del empleado con id=2

for e in empleados:
    if e['id'] == 2:
        # Actualizar el usuario
        e['salario'] = 48000
        break
```

---

## Ejercicios de MongoDB

### Ejercicio 5: Operaciones CRUD

Utilizando la colección `productos`:

```javascript
// Insertar documentos
db.productos.insertMany([
    {"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])

// 1. Read: Encontrar todos los productos de Electrónica
db.productos.find({ categoria: "Electrónica" });

// 2. Read: Encontrar productos con precio < 100
db.productos.find({ precio: { $lt: 100 } });

// 3. Update: Aumentar precio de Laptop en 10%
db.productos.updateOne({ nombre: "Laptop" }, { $mul: { precio: 1.1 } });

// 4. Delete: Eliminar productos con precio < 50
db.productos.deleteMany({ precio: { $lt: 50 } });

// 5. Create: Agregar un nuevo producto
db.productos.insertOne({
  nombre: "Monitor",
  precio: 150,
  categoria: "Electrónica",
});

```

### Ejercicio 6: Consultas Avanzadas en MongoDB

```javascript
// Colección: estudiantes
{"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20}
{"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22}
{"nombre": "Sofia", "materias": ["Biology"], "edad": 19}

// Consultas:
// 1. Encontrar estudiantes que cursan Math
db.estudiantes.find({ materias: "Math" });

// 2. Encontrar estudiantes mayores de 20
db.estudiantes.find({ edad: { $gt: 20 } });

// 3. Contar estudiantes por edad
db.estudiantes.aggregate([
  {
    $group: {
      _id: "$edad",
      totalStudents: { $sum: 1 },
    },
  },
]);

// 4. Proyectar solo nombres
db.estudiantes.find({}, { nombre: 1, _id: 0 });

```

---

## Ejercicios de Investigación

### Ejercicio 7: Tipos de Bases de Datos NoSQL

#### Documentales (MongoDB, CouchDB)

**¿Cuándo usar?**

- Catálogos de productos, CMS, aplicaciones con esquemas de datos que cambian frecuentemente.
**Ventajas**
- Esquema flexible, fácil mapeo con objetos de programación, buena escalabilidad horizontal.
**Desventajas**
- Ineficiente para transacciones complejas o múltiples joins.

#### Key-Value (Redis, DynamoDB.)

**¿Cuándo usar?**

- Sistemas de caché, gestión de sesiones de usuario, carritos de compras.
**Ventajas**
- Extremadamente rápidas, estructura muy simple y fácil de escalar.
**Desventajas**
- No se pueden realizar consultas complejas ni buscar por los valores (solo por la llave).

#### Columnar (Cassandra, HBase)

**¿Cuándo usar?**

- Análisis de Big Data, registros de logs, datos de sensores (IoT) y series temporales.
**Ventajas**
- Excelente rendimiento para consultas de agregación y compresión de datos; altísima disponibilidad.
**Desventajas**
- Actualizar o eliminar registros individuales (filas) es costoso y lento.

#### Graph (Neo4j)

**¿Cuándo usar?**

- Redes sociales, motores de recomendación, detección de fraudes y mapeo de redes.
**Ventajas**
- Rendimiento inigualable para recorrer y consultar relaciones altamente conectadas ycomplejas.
**Desventajas**
- Curva de aprendizaje pronunciada (usan lenguajes como Cypher) y difíciles de escalar horizontalmente.

### Ejercicio 8: Arquitecturas de Almacenamiento

#### ¿Qué es un Data Lake?

Es un gran repositorio centralizado que almacena datos en su formato original y en bruto (estructurados, semiestructurados y no estructurados) sin un propósito predefinido hasta que se necesitan.

#### ¿Qué es un Data Warehouse?

Es un sistema de almacenamiento que contiene datos estructurados, filtrados y procesados específicamente con un propósito predefinido, generalmente para inteligencia de negocios (BI), análisis y creación de reportes.

#### Diferencias entre OLAP y OLTP

- OLTP (Online Transaction Processing): Optimizado para gestionar una alta cantidad de transacciones cortas y rápidas (ej. bases de datos operacionales de un banco). Prioriza la escritura rápida y la integridad de los datos diarios.

- OLAP (Online Analytical Processing): Optimizado para ejecutar consultas complejas de lectura sobre grandes volúmenes de datos históricos (ej. Data Warehouse). Prioriza el análisis y la agregación de datos.

#### ¿Qué es ETL?

Significa Extract, Transform, Load (Extraer, Transformar, Cargar). Es el proceso de integración de datos donde la información se extrae de múltiples fuentes, se transforma (limpia, formatea y consolida) y se carga en un sistema de destino, como un Data Warehouse.
