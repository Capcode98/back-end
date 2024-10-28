from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from sqlalchemy import create_engine
import os


def connecting_bd():

    try:
        engine = create_engine(f'mysql+mysqlconnector://root:{os.environ.get('MYSQL_SECRET')}@localhost/{os.environ.get('MYSQL_DATABASE_NAME')}')
        Session = sessionmaker(bind=engine)
        return Session()
    
    except SQLAlchemyError as e:
        print("Erro ao se conectar com o banco de dados:", e)
        return None