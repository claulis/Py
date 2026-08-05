import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

# SQLite local: nenhuma instalação ou configuração de banco externo é necessária.
DATABASE_URL = "sqlite:///db_pedidos.db"

engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
