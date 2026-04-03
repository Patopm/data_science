# Actividad 2.2: Introducción a MongoDB en macOS

## Requisitos previos

- macOS 10.14 o superior
- [Homebrew](https://brew.sh/) instalado

Para verificar que tienes Homebrew:

```bash
brew --version
```

Si no lo tienes, instálalo con:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## Paso 1: Instalar MongoDB Community Server

**1.1** Agrega el tap oficial de MongoDB a Homebrew:

```bash
brew tap mongodb/brew
```

**1.2** Actualiza Homebrew:

```bash
brew update
```

**1.3** Instala MongoDB Community:

```bash
brew install mongodb-community
```

**1.4** Inicia el servicio de MongoDB:

```bash
brew services start mongodb-community
```

**1.5** Verifica que el servicio esté corriendo:

```bash
brew services list
```

Deberías ver algo así:

```text
Name              Status  User
mongodb-community started tu_usuario
```

---

## Paso 2: Instalar MongoDB Compass

**2.1** Descarga MongoDB Compass desde la página oficial:

[https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)

- Selecciona la versión **macOS**
- Descarga el archivo `.dmg`

**2.2** Abre el archivo `.dmg` descargado y arrastra **MongoDB Compass** a tu carpeta de **Aplicaciones**

**2.3** Abre MongoDB Compass desde el Launchpad o Spotlight (`⌘ + Space` → escribe *Compass*)

**2.4** En la pantalla de conexión, usa la URI por defecto y haz clic en **Connect**:

```text
mongodb://localhost:27017
```

> Si la conexión es exitosa, verás las bases de datos del sistema (`admin`, `config`, `local`)

---

## Paso 3: Crear una base de datos de prueba

**3.1** En MongoDB Compass, haz clic en el botón **"+"** o **"Create Database"**

**3.2** Completa los campos:

- **Database Name:** `actividadDB`
- **Collection Name:** `estudiantes`

**3.3** Haz clic en **"Create Database"**

> MongoDB requiere al menos una colección para crear la base de datos

---

## Paso 4: Crear una colección y agregar 5 documentos

**4.1** Dentro de `actividadDB`, selecciona la colección `estudiantes`

**4.2** Haz clic en **"Add Data"** → **"Insert Document"**

**4.3** Inserta los siguientes 5 documentos uno por uno (o todos a la vez usando el ícono de lista `[]`):

**Documento 1**

```json
{
  "nombre": "Ana García",
  "edad": 21,
  "carrera": "Ingeniería en Sistemas",
  "promedio": 9.2,
  "activo": true
}
```

**Documento 2**

```json
{
  "nombre": "Luis Martínez",
  "edad": 23,
  "carrera": "Ciencias de la Computación",
  "promedio": 8.7,
  "activo": true
}
```

**Documento 3**

```json
{
  "nombre": "Sofía López",
  "edad": 20,
  "carrera": "Ingeniería en Sistemas",
  "promedio": 9.5,
  "activo": true
}
```

**Documento 4**

```json
{
  "nombre": "Carlos Pérez",
  "edad": 24,
  "carrera": "Redes y Telecomunicaciones",
  "promedio": 8.1,
  "activo": false
}
```

**Documento 5**

```json
{
  "nombre": "María Torres",
  "edad": 22,
  "carrera": "Ciencias de la Computación",
  "promedio": 9.0,
  "activo": true
}
```

**4.4** Haz clic en **"Insert"** para confirmar

> Deberías ver los 5 documentos listados en la colección `estudiantes`

---

## Verificación desde la terminal (opcional)

Puedes confirmar todo desde la terminal con el cliente `mongosh`:

```bash
mongosh
```

```bash
use actividadDB
db.estudiantes.find().pretty()
```

Deberías ver los 5 documentos insertados.

---

## Comandos útiles

| Acción | Comando |
| --- | --- |
| Iniciar MongoDB | `brew services start mongodb-community` |
| Detener MongoDB | `brew services stop mongodb-community` |
| Reiniciar MongoDB | `brew services restart mongodb-community` |
| Abrir consola | `mongosh` |
