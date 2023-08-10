from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://U686:U6860712@172.22.135.226:5432/postgres_2"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
db = SessionLocal()

metadata = MetaData(schema = 'omop_v2_reg')

Base = declarative_base(metadata=metadata)  # inherit from this class to create ORM models

def get_db_session():
    session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    db = session()
    try:
        yield db      
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()



    

