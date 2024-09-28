from dao.order_dao import OrderDAO
from dao.product_dao import ProductDAO
from models.order import Order
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class OrderService:
    def __init__(self, order_dao: OrderDAO, product_dao: ProductDAO):
        self.order_dao = order_dao
        self.product_dao = product_dao

    async def create_order(self, order_data: dict) -> Order:
        # Проверка наличия достаточного количества товара
        for item in order_data['items']:
            product = await self.product_dao.get_product(item['product_id'])
            if product.quantity < item['quantity']:
                raise HTTPException(status_code=400, detail="Недостаточно товара на складе")

        order = Order()  # Создаем новый заказ
        for item in order_data['items']:
            order_item = await self.product_dao.get_product(item['product_id'])
            order.items.append(order_item)  # Добавляем элементы заказа

            # Обновляем количество товара на складе
            product.quantity -= item['quantity']
            await self.product_dao.update_product(item['product_id'], {'quantity': product.quantity})

        return await self.order_dao.create_order(order)

    async def get_order(self, order_id: int) -> Order:
        return await self.order_dao.get_order(order_id)

    async def get_all_orders(self) -> list[Order]:
        return await self.order_dao.get_all_orders()

    async def update_order_status(self, order_id: int, status: str) -> Order:
        return await self.order_dao.update_order_status(order_id, status)