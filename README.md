# Curso de Ciencia de Datos

> **Universidad Tecmilenio** — QR.LSTI2309TEO

Monorepo de actividades del curso, organizado con **uv workspaces**.
Cada semana es un proyecto Python independiente con sus propias dependencias.

---

## Estructura del Proyecto

```
data_science/
├── pyproject.toml           # Workspace root (uv)
├── uv.lock                  # Lock file unificado para todo el workspace
├── Makefile                 # Comandos de utilidad
├── docs/                    # Documentación general del curso
│
├── semanas/                 # Un proyecto Python por semana
│   └── semana1/             # Semana 1: Fundamentos y Big Data
│       ├── pyproject.toml   # Dependencias exclusivas de esta semana
│       ├── CONSOLIDADO.md
│       ├── actividad/
│       └── complementarios/
│
└── packages/                # Librerías internas compartidas entre semanas
    ├── ds-mongo/            # Cliente MongoDB reutilizable
    └── ds-postgres/         # Cliente PostgreSQL reutilizable
```

---

## Progreso

- [x] Semana 1: Fundamentos y Big Data
- [ ] Semana 2: Arquitecturas y MongoDB
- [ ] Semana 3: Python y Análisis Exploratorio
- [ ] Semana 4: Preparación de Datos
- [ ] Semana 5: Regresión Lineal Simple
- [ ] Semana 6: Regresión Lineal Múltiple
- [ ] Semana 7: Regresión Logística y Comunicación

---

## Primeros pasos

```bash
# 1. Instalar todas las dependencias del workspace
make install

# 2. Abrir Jupyter para una semana específica
make jupyter-semana1

# 3. Ver todos los comandos disponibles
make help
```

---

## Comandos del Makefile

| Comando | Descripción |
|---|---|
| `make install` | Instala las dependencias de todo el workspace |
| `make sync` | Sincroniza el entorno virtual con el lock file |
| `make jupyter-semana1` | Abre Jupyter Notebook para Semana 1 |
| `make new-semana N=2` | Crea la estructura completa para Semana 2 |
| `make add-dep SEMANA=semana2 PKG=pymongo` | Agrega una dependencia a una semana |
| `make list` | Lista todas las semanas disponibles |
| `make clean` | Elimina caché de Python y Jupyter |

---

## Packages Compartidos

Los paquetes en `packages/` son librerías internas que cualquier semana puede importar.

### Usar un package en una semana

Agrega la dependencia en el `pyproject.toml` de la semana:

```toml
# semanas/semana2/pyproject.toml
[project]
dependencies = [
    "ds-mongo",
]

[tool.uv.sources]
ds-mongo = { workspace = true }
```

O usa el comando de Make:

```bash
make add-dep SEMANA=semana2 PKG=ds-mongo
```

---

## Agregar una nueva semana

```bash
# Crea automáticamente la estructura de carpetas y pyproject.toml
make new-semana N=2

# Luego agrega las dependencias que necesita esa semana
uv add --package semana2 pymongo
```

---

## Variables de entorno

Crea un archivo `.env` en la raíz para configurar las conexiones a bases de datos:

```env
MONGO_URI=mongodb://localhost:27017
POSTGRES_DSN=postgresql://usuario:password@localhost/nombre_db
```
