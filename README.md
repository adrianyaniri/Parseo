# Proyecto Python

Este proyecto utiliza un entorno virtual de Python para gestionar las dependencias.

## Requisitos

- Python 3.x
- Pip (gestor de paquetes de Python)

## Instalación

Sigue estos pasos para configurar el entorno de desarrollo:

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

### 2. Crear un entorno virtual

En Windows:
    ```bash
    python -m venv venv
    ```
En macOS y Linux:
    ```bash
    python3 -m venv venv
    ```
  
### 3. Activar el entorno virtual
En Windows, ejecuta:

```bash
venv\Scripts\activate
```

En macOS y Linux, ejecuta:

```bash
source venv/bin/activate
```
Verás que el nombre del entorno aparece en la terminal, indicando que está activo.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```
Reemplaza <archivo_principal> con el nombre del archivo que inicia tu proyecto.

### 5. Ejecutar el proyecto

Después de instalar las dependencias, puedes ejecutar el proyecto con el siguiente comando:

```bash
python <archivo_principal>.py
```
Reemplaza <archivo_principal> con el nombre del archivo que inicia tu proyecto.

### 6 Desactivar el entorno virtual
Para desactivar el entorno virtual, simplemente ejecuta:
Windows:
```bash
deactivate
```

Linux y macOS:
```bash
source venv/bin/deactivate
```

## Contribuir
Para contribuir, asegúrate de trabajar siempre dentro del entorno virtual 
y actualizar el archivo ***requirements.txt*** 
después de instalar nuevas dependencias con:

```bash
pip freeze > requirements.txt
```