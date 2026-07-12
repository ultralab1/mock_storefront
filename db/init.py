from sqlmodel import Session, SQLModel
from scripts.models import Product, Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

name = "postgres"
uri = f"postgresql+psycopg://user:password@localhost:5432/{name}"
engine = create_engine(uri)

HostSession = sessionmaker(bind=engine)

def init_db():
    SQLModel.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()

