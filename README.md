# SGSI en Python con SQLite

## Descripción
Este proyecto consiste en el desarrollo de un Sistema de Gestión de Seguridad de la Información (SGSI) básico utilizando Python. El sistema permite la gestión de usuarios, autenticación segura, registro de incidentes y generación de reportes, integrando buenas prácticas de seguridad.

## Tecnologías utilizadas
- Python
- SQLite
- hashlib (SHA-256)
- Programación Orientada a Objetos (POO)

## Funcionalidades principales
- Registro de usuarios con validación de contraseña
- Almacenamiento seguro de contraseñas mediante hash SHA-256
- Autenticación de usuarios
- Cambio de contraseña
- Registro de incidentes de seguridad
- Generación de reportes de incidentes
- Persistencia de datos mediante SQLite

## Seguridad implementada
- Hashing de contraseñas (SHA-256)
- Validación de entradas
- Prevención de acceso no autorizado
- Uso de consultas parametrizadas (prevención de SQL Injection)

## Estructura del proyecto
- main.py → punto de entrada
- sistema_sgsi.py → lógica principal
- usuario.py → clase Usuario
- incidente.py → clase Incidente
- database.py → conexión y consultas SQLite
- sgsi.db → base de datos


## Ejecución
1. Clonar el repositorio: git clone https://github.com/alisonguerraaa/SGSI-Python-SQLite.git
2. Ejecutar el sistema: py main.py

## Autores
- Alison Andrea Guerra Gonzalez
- Robert Brian Lowe Camacho

Ingenieria en Sistemas Computacionales