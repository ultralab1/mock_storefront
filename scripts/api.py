from fastapi import FastAPI
from decimal import Decimal
from sqlmodel import Field
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel
from scripts.models import Product, Order
app = FastAPI()

name = "postgres"
uri = f"postgresql+psycopg://user:password@localhost:5432/{name}"
engine = create_engine(uri)

HostSession = sessionmaker(bind=engine)

@app.get("/inventory")
def get_inventory():
    pass

@app.get("/product/{product_id}")
def get_product(product_id: uuid.UUID):
    pass

@app.post("/order")
def order(product_id: uuid.UUID,
          price: Decimal = Field(decimal_places=2)):
    pass

