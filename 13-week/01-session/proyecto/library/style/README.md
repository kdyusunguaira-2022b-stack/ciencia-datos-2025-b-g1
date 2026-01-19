# 📊 Generic Graph Styling Library - Refactored

This library provides **reusable, modular functions** for creating professional visualizations with consistent styling. It has been refactored to work with **any dataset and visualization type**.

## 🎯 Key Features

- ✅ **Generic Functions**: Work with any data, not just student grades
- ✅ **Modular Design**: Small, focused functions that do one thing well
- ✅ **Type Hints**: Full type annotations for better IDE support
- ✅ **Zero Redundancy**: DRY principle applied throughout
- ✅ **Backward Compatible**: Specialized wrappers still available
- ✅ **Highly Customizable**: Accept `**kwargs` for matplotlib parameters

## 📁 Files

```
style/
├── __init__.py                 # Module exports
├── graficas.py                 # Legacy specialized functions
├── function_graph_json.py      # Refactored generic functions
├── README.md                   # This file
├── REFACTOR.md                 # Detailed refactoring documentation
└── examples.py                 # Usage examples
```

## 🚀 Quick Start

### Installation
```python
import sys
sys.path.append('library')

from style import configurar_estilo_global, crear_grafica_barras

# Configure global style
configurar_estilo_global()
```

### Basic Example
```python
# Any bar chart
data = [100, 250, 180, 300]
labels = ['Q1', 'Q2', 'Q3', 'Q4']

fig, ax = crear_grafica_barras(
    data=data,
    labels=labels,
    title='Quarterly Sales',
    xlabel='Quarter',
    ylabel='Sales ($1000)'
)
plt.show()
```

## 📚 Generic Functions (NEW)

### `crear_grafica_barras()`
Create any bar chart with full customization.

```python
fig, ax = crear_grafica_barras(
    data=[10, 20, 15, 25],
    labels=['A', 'B', 'C', 'D'],
    colors=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'],
    title='My Data',
    xlabel='Categories',
    ylabel='Values',
    show_values=True,
    value_format=lambda x: f'{x}%'
)
```

### `crear_grafica_pastel()`
Create any pie chart.

```python
fig, ax = crear_grafica_pastel(
    data=[30, 45, 25],
    labels=['Product A', 'Product B', 'Product C'],
    title='Market Share',
    colors=['#3498db', '#2ecc71', '#e74c3c']
)
```

### `crear_histograma()`
Create histograms with optional threshold coloring.

```python
import numpy as np
data = np.random.normal(100, 15, 500)

fig, ax = crear_histograma(
    data=data,
    bins=20,
    title='Distribution',
    threshold=90,
    threshold_colors={'below': 'red', 'above': 'green'},
    threshold_label='Minimum Standard'
)
```

### `crear_barras_agrupadas()`
Create grouped/clustered bar charts.

```python
data = {
    'Group 1': [10, 20, 30],
    'Group 2': [15, 25, 35],
    'Group 3': [12, 22, 32]
}
labels = ['Cat A', 'Cat B', 'Cat C']

fig, ax = crear_barras_agrupadas(
    data_dict=data,
    labels=labels,
    title='Comparison',
    add_hline=25,
    hline_label='Target'
)
```

## 🎓 Specialized Functions (Student Grades)

For backward compatibility and convenience:

### `grafica_barras_aprobados()`
Crea una gráfica de barras mostrando estudiantes aprobados vs no aprobados.

**Parámetros:**
- `conteo_estado`: Series con el conteo de aprobados y no aprobados
- `total_estudiantes`: Número total de estudiantes
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
conteo = df['Estado'].value_counts()
fig, ax = grafica_barras_aprobados(conteo, len(df))
plt.show()
```

---

### `grafica_pastel_aprobados(conteo_estado, titulo=None, figsize=(8, 8))`
Crea una gráfica de pastel mostrando la proporción de aprobados vs no aprobados.

**Parámetros:**
- `conteo_estado`: Series con el conteo de aprobados y no aprobados
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
conteo = df['Estado'].value_counts()
fig, ax = grafica_pastel_aprobados(conteo)
plt.show()
```

---

### `grafica_histograma_notas(df, columna='Nota_Final', bins=10, titulo=None, figsize=(10, 6))`
Crea un histograma de distribución de notas.

**Parámetros:**
- `df`: DataFrame con los datos
- `columna`: Nombre de la columna con las notas
- `bins`: Número de intervalos
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
fig, ax = grafica_histograma_notas(df, columna='Nota_Final', bins=12)
plt.show()
```

---

### `grafica_barras_por_corte(df, figsize=(12, 6))`
Crea una gráfica de barras agrupadas mostrando las notas por corte de cada estudiante.

**Parámetros:**
- `df`: DataFrame con los datos de estudiantes
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
fig, ax = grafica_barras_por_corte(df)
plt.show()
```

---

### `mostrar_estadisticas_tabla(df)`
Muestra una tabla con estadísticas descriptivas de las notas.

**Parámetros:**
- `df`: DataFrame con los datos de estudiantes

**Uso:**
```python
mostrar_estadisticas_tabla(df)
```

---

### `guardar_grafica(fig, nombre_archivo, carpeta_output='data/output/img', dpi=300)`
Guarda una gráfica en formato PNG y PDF.

**Parámetros:**
- `fig`: Figura de matplotlib a guardar
- `nombre_archivo`: Nombre del archivo (sin extensión)
- `carpeta_output`: Ruta de la carpeta de salida
- `dpi`: Resolución de la imagen

**Uso:**
```python
fig, ax = grafica_barras_aprobados(conteo, len(df))
guardar_grafica(fig, 'grafica_barras_aprobados')
```

---

## 🎨 Colores Disponibles

La biblioteca define una paleta de colores institucionales:

```python
COLORES = {
    'aprobado': '#2ecc71',      # Verde
    'no_aprobado': '#e74c3c',   # Rojo
    'primario': '#3498db',       # Azul
    'secundario': '#9b59b6',     # Morado
    'advertencia': '#f39c12',    # Naranja
    'info': '#1abc9c',           # Turquesa
    'exito': '#27ae60',          # Verde oscuro
    'peligro': '#c0392b'         # Rojo oscuro
}
```

**Uso:**
```python
plt.plot(x, y, color=COLORES['primario'])
```

## 📝 Ejemplo Completo

```python
# 1. Importar y configurar
import sys
sys.path.append('library')
from style import *
configurar_estilo_global()

# 2. Cargar datos
df = pd.read_csv('data/input/data/notas_estudiante.csv')

# 3. Calcular nota final
df['Nota_Final'] = (df['Corte 1'] * 0.3) + (df['Corte 2'] * 0.3) + (df['Corte 3'] * 0.4)
df['Estado'] = df['Nota_Final'].apply(lambda x: 'Aprobado' if x >= 3.0 else 'No Aprobado')

# 4. Crear gráficas
conteo = df['Estado'].value_counts()

# Barras
fig1, ax1 = grafica_barras_aprobados(conteo, len(df))
guardar_grafica(fig1, 'barras_aprobados')
plt.show()

# Pastel
fig2, ax2 = grafica_pastel_aprobados(conteo)
guardar_grafica(fig2, 'pastel_aprobados')
plt.show()

# Histograma
fig3, ax3 = grafica_histograma_notas(df)
guardar_grafica(fig3, 'histograma_notas')
plt.show()

# Estadísticas
mostrar_estadisticas_tabla(df)
```

## 🔧 Personalización

Todas las funciones permiten personalizar:
- Títulos de las gráficas
- Tamaños de las figuras
- Colores (usando la paleta COLORES)
- Rutas de guardado

## 📦 Dependencias

- `matplotlib`
- `seaborn`
- `pandas`
- `numpy`

## 👨‍💻 Autor

Proyecto Corhuila - 2025
