# Reporte Técnico: Estrategia de Datos para DeportivaMX

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Actividad:** Actividad 1 — Ciencia de Datos
**Estudiante:** Patricio Gael Piña Méndez

---

## 1. Perfiles de Ciencia de Datos

Para que DeportivaMX pueda gestionar su crecimiento acelerado y transformar sus datos en decisiones estratégicas, se recomienda la contratación de los siguientes tres perfiles clave, los cuales cubren todo el ciclo de vida del dato:

1. **Ingeniero de Datos (Data Engineer):**
   * **Justificación:** Es el perfil fundamental para iniciar la transformación. DeportivaMX tiene problemas de infraestructura y fuentes de datos dispersas. El Ingeniero de Datos se encargará de diseñar la arquitectura escalable, construir los pipelines (procesos ETL/ELT) para extraer datos de ventas, clientes y productos, y limpiar/organizar esta información en bases de datos eficientes.
2. **Analista de Datos (Data Analyst):**
   * **Justificación:** La empresa requiere explorar los datos y obtener *insights* sobre el comportamiento de sus clientes y el *performance* de la tienda mediante herramientas de visualización. Este perfil creará los *dashboards* y reportes diarios que la gerencia necesita para tomar decisiones rápidas sobre inventario y marketing.
3. **Científico de Datos (Data Scientist):**
   * **Justificación:** Una vez que los datos estén limpios y organizados, el Científico de Datos utilizará modelos matemáticos y de *Machine Learning* para optimizar la experiencia del cliente a mediano plazo. Por ejemplo, podrá crear un sistema de recomendaciones personalizadas de artículos deportivos basado en compras anteriores y predecir tendencias de demanda según la temporada.

---

## 2. Las 5 V del Big Data aplicadas a DeportivaMX

El proyecto de modernización de datos de la tienda cumple con las cinco dimensiones del Big Data de la siguiente manera:

* **Volumen:** DeportivaMX está experimentando un crecimiento masivo en registros. El volumen se refiere al almacenamiento histórico de miles de transacciones diarias, perfiles de clientes, carritos abandonados e inventario general a lo largo del tiempo.
* **Velocidad:** Los datos de la tienda en línea, como los clics de navegación de los usuarios, la búsqueda de artículos y el procesamiento de pagos, se generan en tiempo real o casi en tiempo real. La arquitectura debe poder procesar estos picos de tráfico de manera inmediata, especialmente en épocas de ofertas.
* **Variedad:** La empresa no solo recolecta tablas financieras estructuradas, sino también datos semiestructurados (como catálogos de productos en JSON) y no estructurados (imágenes de los tenis/playeras, reseñas en texto libre de los compradores y logs del servidor).
* **Veracidad:** Para tomar decisiones precisas, la información debe ser confiable. Se aplicarán técnicas de limpieza para eliminar cuentas duplicadas de clientes, bots que inflan las visitas, y asegurar que el inventario reflejado coincida con la realidad.
* **Valor:** Es el objetivo final. Transformar toda esta avalancha de datos de compras e interacciones en estrategias rentables: promociones dirigidas, optimización logística y mejora en la retención de clientes, lo que se traduce directamente en mayores ingresos.

---

## 3. Arquitectura de Almacenamiento

### Arquitectura Propuesta: Data Lakehouse (Agnóstica)

Para una empresa de *e-commerce* con crecimiento acelerado, la arquitectura más óptima es un **Data Lakehouse** implementado en la nube. Esta arquitectura combina la flexibilidad y el bajo costo de un *Data Lake* (para almacenar grandes volúmenes de datos crudos, imágenes de productos y logs en cualquier formato) con el rendimiento estructurado de un *Data Warehouse* (para análisis financieros y BI).

**Ejemplo de implementación en AWS:**

* **Capa de Ingesta y Almacenamiento Raw:** Amazon S3 (Data Lake) para guardar todos los logs, imágenes y archivos crudos de forma económica.
* **Capa Transaccional / Operativa:** Amazon DynamoDB o Amazon DocumentDB (MongoDB compatible) para el catálogo de productos y sesiones de usuarios en tiempo real.
* **Capa Analítica:** Amazon Redshift (Data Warehouse) para centralizar los datos limpios y conectarlos a herramientas de visualización como Amazon QuickSight o Tableau.

### Justificación de la Base de Datos NoSQL

Para el entorno operativo de DeportivaMX, la base de datos más factible a implementar es una **Base de Datos NoSQL orientada a documentos**, específicamente **MongoDB**.

* **¿Por qué?** Un catálogo de artículos deportivos es altamente variable. Unos tenis tienen atributos como "talla" y "tipo de suela", mientras que una raqueta de tenis tiene "tensión de cuerdas" y "peso". Una base de datos relacional tradicional requeriría tablas inmensas con muchos campos vacíos. MongoDB permite almacenar cada producto como un documento JSON independiente con atributos variables, ofreciendo una flexibilidad total para agregar nuevas líneas de productos en el futuro sin romper el esquema. Además, escala horizontalmente de forma nativa para soportar el alto tráfico de usuarios.

---

## 4. Diseño de Colecciones (Estructura para MongoDB)

Para la implementación en MongoDB, se propone el almacenamiento de los datos no estructurados/semiestructurados divididos en tres colecciones principales. Sus estructuras en formato JSON han sido diseñadas y depositadas en el archivo adjunto `colecciones.json`.

Las colecciones definidas son:

1. **Colección `clientes`**: Almacena los datos personales, preferencias deportivas y métodos de contacto de los usuarios.
2. **Colección `productos`**: Gestiona el catálogo de artículos, soportando atributos dinámicos (colores, tallas) mediante *arrays* y subdocumentos.
3. **Colección `ordenes_compra`**: Registra las transacciones, embebiendo los detalles de los productos comprados para agilizar las consultas de lectura de los clientes sobre sus pedidos.
