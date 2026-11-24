# Gestión de Usuarios - Tkinter con POO

Aplicación de escritorio desarrollada en Python con Tkinter implementando arquitectura de separación por capas (`Repository -> Services -> UI`) bajo Programación Orientada a Objetos.

## Funcionalidades

- **Visualización de usuarios:** Tabla tabular (`Treeview`) que muestra `UUID`, `nombre`, `apellido`, `edad` y `email`.
- **Creación de usuarios:** Formulario con validación de datos para registrar nuevos usuarios y actualizar la tabla automáticamente.

## Arrancar la aplicación

```bash
python -B main.py
```
*(En macOS/Linux utiliza `python3 -B main.py`)*

## Estructura del proyecto

```text
proyecto/
├── models/
│   └── user.py
├── repositories/
│   └── user_repository.py
├── services/
│   └── user_service.py
├── ui/
│   └── app_wiki.py
└── main.py
```