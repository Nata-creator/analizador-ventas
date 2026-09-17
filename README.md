# 📊 Analizador de Ventas

Proyecto de análisis de datos desarrollado en Python para procesar información de ventas, obtener métricas comerciales y generar visualizaciones.

## 🚀 Características

* Lectura de datos desde archivos CSV.
* Cálculo de ventas totales.
* Identificación del producto más vendido.
* Cálculo de unidades vendidas.
* Análisis de ventas por categoría.
* Generación automática de gráficos.
* Pruebas automatizadas con pytest.

## 🛠️ Tecnologías utilizadas

* Python
* Pandas
* Matplotlib
* Pytest
* Git

## 📁 Estructura del proyecto

```text
analizador-ventas/
│
├── data/
│   └── ventas.csv
│
├── reports/
│
├── src/
│   ├── analisis.py
│   ├── graficos.py
│   └── main.py
│
├── tests/
│   └── test_analisis.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entra al proyecto:

```bash
cd analizador-ventas
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

Activa el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

Ejecuta el programa desde la raíz del proyecto:

```bash
python src/main.py
```

El programa analizará los datos del archivo:

```text
data/ventas.csv
```

y generará los gráficos dentro de:

```text
reports/
```

## 🧪 Ejecutar las pruebas

Para ejecutar los tests:

```bash
pytest
```

Las pruebas verifican algunas de las principales funciones de análisis del proyecto.

## 📊 Resultados

El proyecto genera visualizaciones a partir de los datos de ventas, incluyendo:

* Ventas por categoría.
* Cantidad de productos vendidos.

## 🎯 Objetivo del proyecto

Este proyecto forma parte de mi portafolio de desarrollo en Python y tiene como objetivo demostrar conocimientos de:

* Manipulación y análisis de datos.
* Programación modular.
* Visualización de datos.
* Testing.
* Control de versiones con Git.

## 👩‍💻 Autor

**Natalia**

Proyecto desarrollado como parte de mi portafolio de Python.
