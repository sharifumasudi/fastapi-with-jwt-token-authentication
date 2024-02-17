from databases import Database
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://root:Developer#1234@localhost/uaa"

app = FastAPI()

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base = declarative_base()