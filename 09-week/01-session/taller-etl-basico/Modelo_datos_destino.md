Modelo de datos destino (PostgreSQL)

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    fecha_registro DATE
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT REFERENCES clientes(id_cliente),
    fecha DATE,
    cantidad INT,
    precio NUMERIC,
    total NUMERIC
);

CREATE TABLE inventario (
    id_producto INT PRIMARY KEY,
    titulo VARCHAR(200),
    autor VARCHAR(100),
    stock INT,
    precio NUMERIC
);
