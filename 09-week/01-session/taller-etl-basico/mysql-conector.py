from sqlalchemy import create_engine, text

USER = "root"
PASSWORD = "Leonardo.29"
HOST = "127.0.0.1"
PORT = 3305
DB = "etl_libreria"

engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

# Probar conexión:
with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE();"))
    print("Conectado a:", result.scalar())
