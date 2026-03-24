# Reporte: Exploración de Fuentes de Datos

## ¿Qué es Kaggle y cómo usarlo?

**Kaggle** es una plataforma en línea que reúne a la comunidad más grande del mundo de científicos de datos y entusiastas del *Machine Learning*.

**Cómo usarlo:**

- **Buscar datos:** Puedes acceder a la pestaña "Datasets" para buscar miles de conjuntos de datos públicos gratuitos sobre casi cualquier tema.
- **Entorno de trabajo:** Permite crear "Notebooks" (cuadernos interactivos en Python o R) directamente en el navegador para analizar los datos sin instalar nada en tu computadora.
- **Descargar:** Puedes descargar los datos (generalmente en formato `.csv`, `.json` o `.xlsx`) para trabajarlos localmente en herramientas como Excel, Power BI o tu propio entorno de programación.
- **Aprender y Competir:** Ofrece minicursos gratuitos y organiza competencias donde las empresas publican un problema y los usuarios compiten por crear el mejor modelo predictivo.

---

## Exploración de 3 Datasets Públicos

A continuación, se presentan tres datasets sencillos y muy populares en la plataforma:

1. **Titanic: Machine Learning from Disaster**
   - **Tipo de datos:** Tabulares (Numéricos y Categóricos).
   - **Contenido:** Información sobre los pasajeros del famoso barco Titanic, como edad, sexo, clase de boleto, tarifa pagada y si sobrevivieron o no al naufragio.

2. **Netflix Movies and TV Shows**
   - **Tipo de datos:** Tabulares (Principalmente texto y datos categóricos).
   - **Contenido:** Un catálogo histórico de las películas y series de televisión disponibles en Netflix, incluyendo directores, elenco, país de origen, año de lanzamiento y clasificación.

3. **Supermarket Sales (Ventas de Supermercado)**
   - **Tipo de datos:** Tabulares (Numéricos, Categóricos y Series de Tiempo).
   - **Contenido:** Registros históricos de ventas de diferentes sucursales de un supermercado durante varios meses. Incluye precios, líneas de productos, métodos de pago y calificación del cliente.

---

## Análisis del Dataset Elegido

**Dataset seleccionado:** *Netflix Movies and TV Shows*

**¿Qué información contiene?**
Este dataset contiene una tabla donde cada fila representa una película o serie de televisión. Las columnas principales incluyen:

- `Type`: Si es película (Movie) o serie (TV Show).
- `Title`: Título de la obra.
- `Director` y `Cast`: Director y actores principales.
- `Country`: País de producción.
- `Release_year`: Año en que se estrenó originalmente.
- `Rating`: Clasificación por edades (ej. TV-MA, PG-13).
- `Listed_in`: Género o categoría (ej. Comedia, Documental).

**¿Qué preguntas podrías responder con estos datos?**
Con esta información, se podría realizar un análisis de datos para responder preguntas como:

1. *¿Qué porcentaje del catálogo de Netflix son Películas frente a Series de TV?*
2. *¿Cuáles son los 5 países que producen la mayor cantidad de contenido para la plataforma?*
3. *¿Cómo ha evolucionado la cantidad de contenido agregado a Netflix año tras año (han subido más cosas recientemente)?*
4. *¿Cuáles son los géneros (categorías) más comunes dentro del catálogo?*
5. *¿Existe alguna relación entre el país de origen y la clasificación por edades del contenido?*
