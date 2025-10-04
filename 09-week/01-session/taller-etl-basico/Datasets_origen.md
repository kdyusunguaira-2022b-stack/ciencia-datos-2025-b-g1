Datasets de origen

- clientes.csv

id_cliente,nombre,email,fecha_registro
1,ana gomez,ana@gmail.com,2024-01-15
2,Luis Perez,luis@gmail.com,2024/02/10
3,Carlos Torres,,2024-03-05
3,Carlos Torres,,2024-03-05

- pedidos.json

[
  {"id_pedido": 101, "id_cliente": 1, "fecha": "2024-03-01", "cantidad": 2, "precio": 50000},
  {"id_pedido": 102, "id_cliente": 2, "fecha": "2024-03-02", "cantidad": 1, "precio": 70000}
]

- inventario (SQLite)

CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    stock INTEGER,
    precio NUMERIC
);

INSERT INTO productos VALUES (1, 'Python Básico', 'J. Perez', 10, 50000);
INSERT INTO productos VALUES (2, 'Data Science 101', 'M. García', 5, 70000);

