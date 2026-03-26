# Reporte: Investigación de Arquitecturas de Datos

## ¿Qué son los Data Warehouses y Data Lakes?

**Data Warehouse (Almacén de Datos)**
Es un sistema diseñado para el análisis y la elaboración de informes de datos empresariales. Centraliza datos de diversas fuentes operativas, los limpia y los organiza de manera estructurada. Se basa en el esquema de "Schema-on-write", lo que significa que los datos deben ser modelados y definidos antes de ser cargados.

**Data Lake (Lago de Datos)**
Es un repositorio centralizado que permite almacenar todos los datos, tanto estructurados como no estructurados (imágenes, PDFs, logs, redes sociales), a cualquier escala. Utiliza el esquema de "Schema-on-read", es decir, los datos se guardan en su formato nativo y se les da estructura solo cuando se necesitan para una consulta o análisis.

---

## Comparación de Características

| Característica | Data Warehouse | Data Lake |
| --- | --- | --- |
| Tipo de datos| Solo estructurados (tablas). | Estructurados, semiestructurados y no estructurados. |
| Propósito | Reportes de negocio, BI y KPIs definidos. | Análisis predictivo, Machine Learning, exploración de datos. |
| Usuarios | Analistas de negocio y usuarios finales. | Científicos de datos e ingenieros de datos. |
| Costo | Alto (debido al procesamiento previo y almacenamiento especializado). | Bajo (almacenamiento en bruto más económico). |
| Agilidad | Baja (cambiar el esquema requiere mucho esfuerzo). |  Alta (se adapta fácilmente a nuevos tipos de datos). |

---

## ¿Qué es un Data Mart?

Un Data Mart es una versión enfocada de un Data Warehouse que contiene un subconjunto de datos específicos para un área, departamento o unidad de negocio particular (por ejemplo: Ventas, Marketing o Recursos Humanos).

- Propósito: Facilitar que un grupo específico de usuarios acceda a los datos exactos que necesitan sin tener que buscar en toda la base de datos corporativa.

- Origen: Puede ser dependiente (se extrae de un Data Warehouse global) o independiente (se crea directamente de fuentes operativas).

---

## Diagrama de Diferencias y Flujo

A continuación se presenta un diagrama textual que ilustra cómo fluyen los datos en estas arquitecturas:

```txt
 FUENTES DE DATOS         ALMACENAMIENTO                      SALIDA / USO
 (ERP, CRM, Logs)

 [ Datos Brutos ] ------> [ DATA LAKE ] -------------------> (Ciencia de Datos)
       |                (Datos sin procesar)                 (Machine Learning)
       |
       |       ETL
       V    (Limpieza)
 [ Proceso ETL ] -------> [ DATA WAREHOUSE ] --------------> (Business Intelligence)
                          (Datos Estructurados)             (Reportes Globales)
                                  |
                                  |--- [ Data Mart Ventas ] -> (Analistas Ventas)
                                  |
                                  |--- [ Data Mart RH ] -----> (Analistas RH)
```

Resumen del flujo:

1. Los datos del Data Lake se mantienen en bruto para análisis avanzados.

2. Los datos del Data Warehouse pasan por un proceso de transformación (ETL) para asegurar su calidad.

3. Los Data Marts actúan como "tiendas especializadas" que toman la información relevante del Warehouse para equipos específicos.
