from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        orm_mode = True  # Позволяет использовать ORM-объекты