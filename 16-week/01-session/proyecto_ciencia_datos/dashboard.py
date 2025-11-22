import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Cargar dataset (debe estar en la misma carpeta)
df = pd.read_csv("dataset.csv", parse_dates=["fecha"])

# Métricas
ventas_totales = df["ventas"].sum()
ventas_mensuales = df.resample("M", on="fecha")["ventas"].sum().reset_index()
promedio_mensual = ventas_mensuales["ventas"].mean()
top5 = df.groupby("producto")["ventas"].sum().sort_values(ascending=False).head(5)

# 1) Gráfico de barras - Top 5 productos
fig1 = px.bar(
    top5.reset_index(),
    x="producto",
    y="ventas",
    title="Top 5 Productos Más Vendidos",
    labels={"ventas":"Ventas", "producto":"Producto"}
)

# 2) Serie temporal - Ventas mensuales
ventas_mensuales["mes"] = ventas_mensuales["fecha"].dt.strftime("%b")

fig2 = px.line(
    ventas_mensuales,
    x="mes",
    y="ventas",
    title="Evolución Mensual de Ventas",
    markers=True
)

fig2.update_layout(
    template="simple_white",
    yaxis_title="Ventas",
    xaxis_title="Mes",
)

# 3) Ventas por región (scatter)
fig3 = px.scatter(
    df,
    x="fecha",
    y="ventas",
    color="region",
    title="Ventas por Región",
    hover_data=["producto","cliente"]
)

# 4) KPI indicador
fig4 = go.Figure()  
fig4.add_trace(go.Indicator(
    mode="number+delta",
    value=ventas_totales,
    number={"prefix":"$"},
    delta={"reference": promedio_mensual},
    title={"text":"Ventas Totales (delta vs promedio mensual)"}
))

# Mostrar figuras
fig4.show()
fig1.show()
fig2.show()
fig3.show()

# Guardar dashboard HTML
html_parts = []
for fig in [fig4, fig1, fig2, fig3]:
    html_parts.append(pio.to_html(fig, full_html=False, include_plotlyjs=False))

html_template = """
<html>
<head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<title>Dashboard de Ventas</title>
</head>
<body>
<h1>Dashboard de Ventas</h1>
{content}
</body>
</html>
"""

html_content = html_template.format(content="<hr>".join(html_parts))
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Dashboard generado como: dashboard.html")
