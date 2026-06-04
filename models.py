from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    descr: str
    price: float
    quantity: int


