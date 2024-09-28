from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItem]

class OrderOut(BaseModel):
    id: int
    created_date: str  # Или datetime
    status: str
    items: List[OrderItem]

    class Config:
        orm_mode = True  # Позволяет использовать ORM-объекты