from sqlmodel import Session, SQLModel
from scripts.models import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

name = "storefront"
uri = f"postgresql+psycopg://user:password@localhost:5432/{name}"
engine = create_engine(uri)

HostSession = sessionmaker(bind=engine)

def init_db():
    SQLModel.metadata.create_all(bind=engine)

init_db()

