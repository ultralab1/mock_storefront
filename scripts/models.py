from sqlmodel import SQLModel, Field
from decimal import Decimal
import uuid
from datetime import datetime, timezone

class Product(SQLModel, table=True):
    __tablename__ = "products"
    product_id: int = Field(primary_key=True)
    name: str
    price: Decimal = Field(decimal_places=2)
    image: bytes                                    # Inefficient for production, preferably store URLs, but I don't
    inventory: int                                  # have a server or CDN to store/serve images
    digital: bool

class Order(SQLModel, table=True):
    __tablename__ = "orders"
    order_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    quantity: int
    total: int = Field(primary_key=True)
    ordered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    product_id: int = Field(foreign_key="products.product_id")

