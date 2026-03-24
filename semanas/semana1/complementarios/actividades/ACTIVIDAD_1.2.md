# Reporte: Casos de Uso de Ciencia de Datos en la Industria

## Netflix

Netflix es pionero en el uso de datos para transformar la industria del entretenimiento, pasando de ser un distribuidor de DVD a un gigante del streaming y la producción de contenido.

* **Tipos de datos que recopilan:**
  * Historial de visualización (qué ves, cuándo lo ves, en qué dispositivo).
  * Interacciones con la plataforma (pausas, retrocesos, saltos de introducciones).
  * Búsquedas realizadas y calificaciones otorgadas.
  * Tiempo de navegación antes de seleccionar un título.
* **Técnicas de análisis utilizadas:**
  * **Filtrado Colaborativo y Basado en Contenido:** Para recomendar series o películas con base en usuarios similares o atributos del contenido.
  * **Pruebas A/B (A/B Testing):** Para optimizar desde la interfaz de usuario hasta las imágenes en miniatura (thumbnails) que se muestran para cada título.
  * **Modelos Predictivos (Machine Learning):** Para predecir el éxito de una posible serie antes de producirla.
* **Problemas que resuelven con los datos:**
  * **Retención de usuarios:** El sistema de recomendación altamente personalizado evita que los usuarios cancelen su suscripción por "falta de contenido".
  * **Toma de decisiones de producción:** Decidir qué series o películas originales crear basándose en los gustos exactos de su audiencia (ej. *House of Cards* o *Stranger Things*).
  * **Optimización de red:** Predecir qué servidores necesitarán almacenar qué películas según la demanda geográfica para evitar interrupciones de carga (buffering).

---

## Amazon

Amazon utiliza la ciencia de datos en cada etapa del viaje del cliente, desde que entra a la página web hasta que el paquete llega a su puerta.

* **Tipos de datos que recopilan:**
  * Historial de compras y productos vistos.
  * Artículos abandonados en el carrito de compras o guardados para más tarde.
  * Direcciones de envío, tiempos de entrega y métodos de pago.
  * Reseñas de productos y comportamiento en búsquedas.
* **Técnicas de análisis utilizadas:**
  * **Análisis de la Cesta de la Compra (Association Rules):** Identificar qué productos se compran frecuentemente juntos.
  * **Análisis de Series Temporales (Time-Series Forecasting):** Predecir la demanda futura de productos específicos.
  * **Procesamiento de Lenguaje Natural (NLP):** Para analizar el sentimiento de las reseñas y potenciar a su asistente de voz, Alexa.
* **Problemas que resuelven con los datos:**
  * **Venta cruzada y Venta adicional (Cross-selling / Up-selling):** El motor de recomendaciones ("Los clientes que compraron este producto también compraron...") genera una gran parte de sus ingresos totales.
  * **Optimización de la cadena de suministro:** Amazon anticipa la demanda de ciertos productos en regiones específicas y los envía a los almacenes más cercanos incluso antes de que el cliente realice la compra.
  * **Precios dinámicos:** Ajustar los precios millones de veces al día en función de la demanda, la competencia y el inventario.

---

## Spotify

El éxito de Spotify radica en su capacidad para ofrecer a los usuarios música nueva que les encantará, creando una experiencia altamente inmersiva y adictiva.

* **Tipos de datos que recopilan:**
  * Historial de reproducción y canciones saltadas (skips).
  * Listas de reproducción creadas por los usuarios.
  * Hora del día y contexto de escucha (ej. escuchar música de gimnasio por la mañana).
  * Interacciones sociales (canciones compartidas con amigos).
* **Técnicas de análisis utilizadas:**
  * **Filtrado Colaborativo:** Compara tus hábitos de escucha con los de millones de usuarios para encontrar patrones.
  * **Procesamiento de Lenguaje Natural (NLP):** Rastrea blogs, artículos y redes sociales en internet para entender cómo se describe y clasifica la música o los artistas actualmente.
  * **Análisis de Audio en Crudo (Redes Neuronales Convolucionales):** Analiza las características acústicas de una canción (tempo, energía, tono) para recomendar canciones que suenan parecido, incluso si el artista es completamente desconocido.
* **Problemas que resuelven con los datos:**
  * **Descubrimiento de contenido:** Su funcionalidad de "Descubrimiento Semanal" mantiene a los usuarios enganchados al ofrecer nueva música con un alto índice de acierto.
  * **Segmentación de anuncios:** Para los usuarios del modelo gratuito, utilizan los datos de escucha para inferir datos demográficos, estados de ánimo y rutinas, sirviendo anuncios altamente dirigidos para sus anunciantes.
