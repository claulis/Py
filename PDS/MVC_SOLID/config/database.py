from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/db_pedidos"

engine = create_engine(DATABASE_URL, echo=False, isolation_level="AUTOCOMMIT")
SessionLocal = sessionmaker(bind=engine)