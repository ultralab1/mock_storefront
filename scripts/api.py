from fastapi import FastAPI
from decimal import Decimal
from sqlmodel import Field
import uuid

app = FastAPI()

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

