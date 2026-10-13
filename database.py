from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://demo:demo@localhost:5432/demo_persons"

engine = create_engine(DATABASE_URL, echo=False)  # Affiche les requêtes SQL

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
