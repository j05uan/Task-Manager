# Aquí configuramos la conexión con la base de datos y la creación de tablas

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Aquí la conexión está algo suelta y desordenada, pero funciona
DATABASE_URL = 'sqlite:///tasks.db'  # Usamos SQLite por ahora (pero se puede cambiar por PostgreSQL)

engine = create_engine(DATABASE_URL)  # Creamos el motor de la base de datos
Session = sessionmaker(bind=engine)  # Creamos la sesión para interactuar con la base de datos

# Esto crea las tablas si no existen (aunque en este punto podría ser más limpio)
Base.metadata.create_all(engine)  # Crea las tablas de la base de datos
