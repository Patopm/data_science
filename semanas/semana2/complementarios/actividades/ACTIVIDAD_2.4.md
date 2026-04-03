# Actividad 2.4: Modelado de Datos NoSQL

## Sistema de Biblioteca Digital

---

## 1. Introducción

Este documento describe el diseño de un modelo de datos NoSQL orientado a documentos para un **Sistema de Biblioteca Digital**.

Se priorizó la lectura eficiente, la desnormalización y la flexibilidad de esquema propia de este paradigma.

---

## 2. Colecciones y Estructura de Documentos

### 2.1 `usuarios`

Representa a los usuarios registrados en la plataforma.

```json
{
  "_id": "ObjectId('64a1f2c3e4b0a1b2c3d4e5f6')",
  "nombre": "Ana García",
  "email": "ana.garcia@email.com",
  "password_hash": "bcrypt:$2b$12$...",
  "rol": "lector",
  "activo": true,
  "fecha_registro": "ISODate('2024-03-15T10:30:00Z')",
  "perfil": {
    "avatar_url": "https://cdn.biblioteca.mx/avatars/ana.jpg",
    "biografia": "Apasionada por la literatura latinoamericana.",
    "preferencias_genero": ["ficción", "historia", "ciencia"],
    "idioma_preferido": "es"
  },
  "suscripcion": {
    "tipo": "premium",
    "fecha_inicio": "ISODate('2024-01-01T00:00:00Z')",
    "fecha_fin": "ISODate('2025-01-01T00:00:00Z')",
    "activa": true
  },
  "estadisticas": {
    "libros_leidos": 42,
    "paginas_leidas": 12480,
    "tiempo_lectura_minutos": 8760
  }
}
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `_id` | ObjectId | Identificador único |
| `nombre` | String | Nombre completo |
| `email` | String | Único, indexado |
| `rol` | String | `lector`, `admin`, `editor` |
| `activo` | Boolean | Estado de la cuenta |
| `perfil` | Object | Datos opcionales embebidos |
| `suscripcion` | Object | Plan activo embebido |
| `estadisticas` | Object | Contadores actualizados en tiempo real |

---

### 2.2 `libros`

Catálogo central de la biblioteca digital.

```json
{
  "_id": "ObjectId('74b2a3d4e5c6f7a8b9c0d1e2')",
  "isbn": "978-0-06-112008-4",
  "titulo": "Cien Años de Soledad",
  "slug": "cien-anos-de-soledad",
  "autores": [
    {
      "autor_id": "ObjectId('84c3b4e5f6d7a8b9c0d1e2f3')",
      "nombre": "Gabriel García Márquez",
      "rol": "autor_principal"
    }
  ],
  "editorial": {
    "editorial_id": "ObjectId('94d4c5f6a7e8b9c0d1e2f3a4')",
    "nombre": "Editorial Sudamericana",
    "pais": "Argentina"
  },
  "generos": ["ficción", "realismo mágico", "novela"],
  "etiquetas": ["clásico", "latinoamérica", "siglo XX"],
  "idioma": "es",
  "fecha_publicacion": "ISODate('1967-05-30T00:00:00Z')",
  "fecha_ingreso_catalogo": "ISODate('2023-01-10T00:00:00Z')",
  "descripcion": "La historia de la familia Buendía...",
  "portada_url": "https://cdn.biblioteca.mx/portadas/cien-anos.jpg",
  "paginas": 471,
  "formatos_disponibles": ["epub", "pdf", "audiobook"],
  "archivos": {
    "epub": "https://storage.biblioteca.mx/libros/cien-anos.epub",
    "pdf": "https://storage.biblioteca.mx/libros/cien-anos.pdf",
    "audiobook": "https://storage.biblioteca.mx/libros/cien-anos.mp3"
  },
  "calificacion_promedio": 4.8,
  "total_resenas": 1240,
  "total_prestamos": 8530,
  "disponible": true,
  "destacado": true
}
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `_id` | ObjectId | Identificador único |
| `isbn` | String | Único, indexado |
| `autores` | Array\<Object\> | Referencias parciales desnormalizadas |
| `editorial` | Object | Referencia parcial desnormalizada |
| `generos` | Array\<String\> | Indexado para búsquedas |
| `formatos_disponibles` | Array\<String\> | Formatos del libro |
| `archivos` | Object | URLs por formato |
| `calificacion_promedio` | Number | Calculado y cacheado |

---

### 2.3 `autores`

Información detallada de los autores del catálogo.

```json
{
  "_id": "ObjectId('84c3b4e5f6d7a8b9c0d1e2f3')",
  "nombre_completo": "Gabriel José de la Concordia García Márquez",
  "nombre_display": "Gabriel García Márquez",
  "nacionalidad": "Colombiano",
  "fecha_nacimiento": "ISODate('1927-03-06T00:00:00Z')",
  "fecha_fallecimiento": "ISODate('2014-04-17T00:00:00Z')",
  "biografia": "Escritor, novelista, cuentista, guionista...",
  "foto_url": "https://cdn.biblioteca.mx/autores/ggm.jpg",
  "redes_sociales": {
    "twitter": null,
    "instagram": null,
    "wikipedia": "https://es.wikipedia.org/wiki/Gabriel_García_Márquez"
  },
  "premios": [
    {
      "nombre": "Premio Nobel de Literatura",
      "anio": 1982,
      "institucion": "Academia Sueca"
    }
  ],
  "generos_principales": ["realismo mágico", "ficción"],
  "total_libros_en_catalogo": 12,
  "calificacion_promedio_obras": 4.7
}
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `_id` | ObjectId | Identificador único |
| `nombre_display` | String | Nombre público, indexado |
| `premios` | Array\<Object\> | Embebido por baja frecuencia de cambio |
| `total_libros_en_catalogo` | Number | Contador cacheado |

---

### 2.4 `prestamos`

Registro de accesos y préstamos activos/históricos de los usuarios.

```json
{
  "_id": "ObjectId('a1b2c3d4e5f6a7b8c9d0e1f2')",
  "usuario_id": "ObjectId('64a1f2c3e4b0a1b2c3d4e5f6')",
  "usuario_nombre": "Ana García",
  "libro_id": "ObjectId('74b2a3d4e5c6f7a8b9c0d1e2')",
  "libro_titulo": "Cien Años de Soledad",
  "libro_portada": "https://cdn.biblioteca.mx/portadas/cien-anos.jpg",
  "formato": "epub",
  "estado": "activo",
  "fecha_prestamo": "ISODate('2024-11-01T14:20:00Z')",
  "fecha_vencimiento": "ISODate('2024-11-15T14:20:00Z')",
  "fecha_devolucion": null,
  "progreso": {
    "pagina_actual": 230,
    "porcentaje": 48.8,
    "ultimo_acceso": "ISODate('2024-11-10T21:05:00Z')",
    "tiempo_total_lectura_minutos": 420
  },
  "dispositivos_usados": ["web", "mobile_android"],
  "renovaciones": 1,
}
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `_id` | ObjectId | Identificador único |
| `usuario_id` | ObjectId | Referencia a `usuarios` |
| `libro_id` | ObjectId | Referencia a `libros` |
| `usuario_nombre` | String | Desnormalizado para evitar joins |
| `libro_titulo` | String | Desnormalizado para evitar joins |
| `estado` | String | `activo`, `vencido`, `devuelto` |
| `progreso` | Object | Tracking de lectura embebido |

---

### 2.5 `resenas`

Reseñas y calificaciones de los usuarios sobre los libros.

```json
{
  "_id": "ObjectId('b2c3d4e5f6a7b8c9d0e1f2a3')",
  "libro_id": "ObjectId('74b2a3d4e5c6f7a8b9c0d1e2')",
  "libro_titulo": "Cien Años de Soledad",
  "usuario_id": "ObjectId('64a1f2c3e4b0a1b2c3d4e5f6')",
  "usuario_nombre": "Ana García",
  "usuario_avatar": "https://cdn.biblioteca.mx/avatars/ana.jpg",
  "calificacion": 5,
  "titulo_resena": "Una obra que cambia la perspectiva",
  "contenido": "Pocas veces un libro logra transportarte tan completamente...",
  "contiene_spoilers": false,
  "idioma": "es",
  "fecha_creacion": "ISODate('2024-11-12T09:15:00Z')",
  "fecha_modificacion": "ISODate('2024-11-12T09:15:00Z')",
  "util_votos": 87,
  "no_util_votos": 3,
  "estado": "publicada",
  "respuesta_editorial": null,
  "etiquetas_usuario": ["emotivo", "profundo", "recomendado"]
}
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `_id` | ObjectId | Identificador único |
| `libro_id` | ObjectId | Referencia a `libros`, indexado |
| `usuario_id` | ObjectId | Referencia a `usuarios`, indexado |
| `calificacion` | Number | Entero del 1 al 5 |
| `estado` | String | `publicada`, `moderacion`, `eliminada` |
| `util_votos` | Number | Contador de votos positivos |

---

## 3. Diagrama de Relaciones

```text
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   usuarios  │──────▶│  prestamos  │◀──────│    libros   │
└─────────────┘  1:N  └─────────────┘  N:1  └──────┬──────┘
       │                                            │
       │  1:N          ┌─────────────┐              │ N:M
       └──────────────▶│   resenas   │              │
                       └─────────────┘       ┌──────▼──────┐
                                             │   autores   │
                                             └─────────────┘
```

---

## 4. Índices Recomendados

```js
// usuarios
db.usuarios.createIndex({ email: 1 }, { unique: true });
db.usuarios.createIndex({ "suscripcion.activa": 1, rol: 1 });

// libros
db.libros.createIndex({ isbn: 1 }, { unique: true });
db.libros.createIndex({ slug: 1 }, { unique: true });
db.libros.createIndex({ generos: 1 });
db.libros.createIndex({ titulo: "text", descripcion: "text" }); // búsqueda full-text
db.libros.createIndex({ calificacion_promedio: -1 });

// prestamos
db.prestamos.createIndex({ usuario_id: 1, estado: 1 });
db.prestamos.createIndex({ libro_id: 1 });
db.prestamos.createIndex({ fecha_vencimiento: 1 }, { expireAfterSeconds: 0 });

// resenas
db.resenas.createIndex({ libro_id: 1, estado: 1 });
db.resenas.createIndex({ usuario_id: 1 });
db.resenas.createIndex({ libro_id: 1, calificacion: -1 });
```

---

## 5. Justificación del Diseño

### 5.1 Elección de NoSQL orientado a documentos

| Criterio | Justificación |
| --- | --- |
| **Esquema flexible** | Los libros pueden tener metadatos muy distintos (audiobooks vs ebooks vs PDF) |
| **Lecturas frecuentes** | La biblioteca prioriza consultas de catálogo sobre escrituras |
| **Escalabilidad horizontal** | El volumen de libros, usuarios y préstamos puede crecer masivamente |
| **Datos heterogéneos** | Cada autor, libro o usuario puede tener campos opcionales únicos |

### 5.2 Desnormalización controlada

En documentos como `prestamos` y `resenas` se repiten campos como `usuario_nombre` o `libro_titulo`. Esto es **intencional**:

- Evita *joins* costosos en consultas frecuentes (ej. historial de un usuario).
- Acepta el trade-off: si el nombre cambia, se actualiza con una operación `updateMany` acotada.
- Los datos desnormalizados son de **baja frecuencia de cambio**.

### 5.3 Embedding vs Referencia

| Decisión | Estrategia | Razón |
| --- | --- | --- |
| `perfil` en `usuarios` | **Embebido** | Siempre se carga junto al usuario |
| `suscripcion` en `usuarios` | **Embebido** | 1:1, datos cohesivos |
| `progreso` en `prestamos` | **Embebido** | Alta cohesión con el préstamo |
| `premios` en `autores` | **Embebido** | Lista pequeña y estática |
| `autores` en `libros` | **Referencia parcial** | Evita duplicar biografías largas |
| `resenas` | **Colección separada** | Alto volumen, consultas independientes |
| `prestamos` | **Colección separada** | Historial creciente y consultas propias |

### 5.4 Campos calculados/cacheados

Campos como `calificacion_promedio`, `total_libros_leidos` o `total_prestamos` se **calculan y almacenan** en lugar de computarse en cada consulta, usando operaciones de actualización con `$inc` al momento de cada evento. Esto reduce la carga en lecturas a costa de mayor complejidad en escrituras.

---

## 6. Conclusión

El modelo diseñado aprovecha las fortalezas de NoSQL documental:

- Lecturas rápidas con datos embebidos cohesivos
- Flexibilidad para extender campos sin migraciones
- Escalabilidad para millones de libros y usuarios
- Consultas eficientes mediante índices estratégicos
- Desnormalización justificada con datos de baja mutabilidad
