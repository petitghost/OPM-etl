from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "oracle://cird:cird2033@dws.vghtc.gov.tw:1521/dws"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
db = SessionLocal()

metadata = MetaData(schema = 'OPDUSR')

Base = declarative_base(metadata=metadata)  # inherit from this class to create ORM models

def get_oracle_session():
    session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    db = session()
    try:
        yield db      
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

