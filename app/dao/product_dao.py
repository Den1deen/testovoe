from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.product import Product

class ProductDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(self, product: Product) -> Product:
        self.db.add(product)
        await self.db.commit()  # Асинхронное подтверждение транзакции
        await self.db.refresh(product)  # Обновляем объект после создания
        return product

    async def get_product(self, product_id: int) -> Product:
        return await self.db.get(Product, product_id)  # Получаем продукт по ID

    async def get_all_products(self) -> list[Product]:
        result = await self.db.execute(select(Product))
        return result.scalars().all()  # Возвращаем список всех продуктов

    async def update_product(self, product_id: int, product_data: dict) -> Product:
        product = await self.get_product(product_id)
        for key, value in product_data.items():
            setattr(product, key, value)  # Обновляем свойства
        await self.db.commit()
        return product

    async def delete_product(self, product_id: int):
        product = await self.get_product(product_id)
        await self.db.delete(product)  # Удаляем продукт
        await self.db.commit()  # Подтверждаем изменения