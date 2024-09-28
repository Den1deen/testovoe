from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Order

class OrderDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_order(self, order: Order) -> Order:
        self.db.add(order)
        await self.db.commit()
        await self.db.refresh(order)
        return order

    async def get_order(self, order_id: int) -> Order:
        return await self.db.get(Order, order_id)

    async def get_all_orders(self) -> list[Order]:
        result = await self.db.execute(select(Order))
        return result.scalars().all()

    async def update_order_status(self, order_id: int, status: str) -> Order:
        order = await self.get_order(order_id)
        order.status = status
        await self.db.commit()
        return order