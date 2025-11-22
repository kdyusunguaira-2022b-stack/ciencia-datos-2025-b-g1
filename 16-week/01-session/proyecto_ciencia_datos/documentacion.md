# Documentación del Tablero - Proyecto Unidad 3
Sustentado por: Karol Dayana Yusunguaira Murcia 

## 1. Objetivo del trabajo
Este proyecto se cumple sobre la creación de tableros interactivos.  
El tablero se construyó en Python utilizando Plotly y Pandas.

## 2. Descripción del dataset
El archivo `dataset.csv` contiene datos sintéticos de ventas del 2024.  
Columnas:
- fecha
- producto
- cliente
- region
- ventas

El dataset permite calcular métricas de desempeño comercial como ventas mensuales, productos más vendidos y comportamiento por región.

## 3. Métricas implementadas
- Ventas totales.
- Promedio mensual de ventas.
- Top 5 productos más vendidos.
- Ventas por región.
- KPI comparativo de desempeño.

## 4. Visualizaciones del tablero
1. **Gráfico de barras**: top 5 productos.
2. **Serie temporal**: evolución mensual de ventas.
3. **Scatter**: ventas por región.
4. **KPI**: ventas totales vs promedio mensual.

## 5. Cómo ejecutar el tablero
1. Ubicar `dataset.csv` y `dashboard.py` en la misma carpeta.
2. Instalar dependencias:
pip install pandas plotly
3. Ejecutar:
python dashboard.py
4. Se generará `dashboard.html`, un tablero totalmente interactivo.

## 6. Archivos del proyecto
- dataset.csv  
- dashboard.py  
- Documentacion.md  
- Reflexion.md  
- dashboard.html (generado al ejecutar el script)
