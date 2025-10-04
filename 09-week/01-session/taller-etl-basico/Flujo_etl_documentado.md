1. Flujo ETL documentado

Escenario:
La empresa ficticia Librería Estudiantil quiere integrar la información de clientes, pedidos e inventario para centralizarla en una base de datos PostgreSQL.

ETL propuesto:

Extract: Se leen datos desde un CSV (clientes), un JSON (pedidos) y una base SQLite (inventario).

Transform: Se limpian duplicados, se corrigen nombres, se estandarizan fechas y se calculan métricas (ej. valor total del pedido).

Load: Los datos procesados se cargan en PostgreSQL en tres tablas (clientes, pedidos, inventario).