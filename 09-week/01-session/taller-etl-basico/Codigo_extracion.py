import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# ----------------- EXTRACCIÓN -----------------
clientes = pd.read_csv("clientes.csv")              # CSV
pedidos = pd.read_json("pedidos.json")              # JSON
con = sqlite3.connect("inventario.db")              # SQL
inventario = pd.read_sql("SELECT * FROM productos", con)

# ----------------- TRANSFORMACIÓN -----------------
clientes.drop_duplicates(inplace=True)
clientes.dropna(subset=["email"], inplace=True)
clientes["nombre"] = clientes["nombre"].str.title()
clientes["fecha_registro"] = pd.to_datetime(clientes["fecha_registro"], errors="coerce")

pedidos["fecha"] = pd.to_datetime(pedidos["fecha"], errors="coerce")
pedidos["total"] = pedidos["cantidad"] * pedidos["precio"]

# ----------------- CARGA -----------------
engine = create_engine("mysql+mysqlconnector://root:Leonardo29@localhost:3305/etl_libreria")

clientes.to_sql("clientes", engine, if_exists="replace", index=False)
pedidos.to_sql("pedidos", engine, if_exists="replace", index=False)
inventario.to_sql("inventario", engine, if_exists="replace", index=False)

print("Flujo ETL ejecutado con éxito 🚀")
