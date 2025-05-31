from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

 
connection_uri = (
    "mssql+pyodbc://@SUBBUCHAND19\\SQLEXPRESS/TestDB?driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(connection_uri)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
 
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()