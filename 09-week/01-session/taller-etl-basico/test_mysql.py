import mysql.connector

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leonardo.29"  # cámbiala por la que usas en Workbench
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES;")

print("Bases de datos disponibles en MySQL:")
for db in cursor:
    print(db)

conn.close()
