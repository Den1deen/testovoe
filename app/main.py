from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Config
from models.product import Base as ProductBase
from models.order import Base as OrderBase
from api import products, orders
from database import get_db, engine


# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Регистрируем маршруты
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])

# Создаем все таблицы
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(ProductBase.metadata.create_all)
        await conn.run_sync(OrderBase.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()