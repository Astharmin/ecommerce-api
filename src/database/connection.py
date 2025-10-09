from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./ecommerce.db"  # Cambiar a la URL de la base de datos deseada

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Importa aquí todos tus modelos para que SQLAlchemy registre las tablas
    # Ejemplo:
    # from src.models.product import Product
    # from src.models.user import User
    # from src.models.order import Order
    # Agrega aquí todos los modelos que tengas

    Base.metadata.create_all(bind=engine)