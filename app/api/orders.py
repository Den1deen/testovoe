from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.order_service import OrderService
from dao.order_dao import OrderDAO
from dao.product_dao import ProductDAO
from database import get_db
from schemas.order_schema import OrderCreate, OrderOut

router = APIRouter()

@router.post("/orders/", response_model=OrderOut)
async def create_order(order_data: OrderCreate, db: AsyncSession = Depends(get_db)):
    """
    Создает новый заказ, проверяя наличие достаточного количества товара.
    """
    order_service = OrderService(OrderDAO(db), ProductDAO(db))
    return await order_service.create_order(order_data.dict())

@router.get("/orders/", response_model=list[OrderOut])
async def get_all_orders(db: AsyncSession = Depends(get_db)):
    """
    Возвращает список всех заказов.
    """
    order_service = OrderService(OrderDAO(db), ProductDAO(db))
    return await order_service.get_all_orders()

@router.get("/orders/{id}", response_model=OrderOut)
async def get_order(id: int, db: AsyncSession = Depends(get_db)):
    """
    Возвращает информацию о заказе по ID.
    """
    order_service = OrderService(OrderDAO(db), ProductDAO(db))
    order = await order_service.get_order(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/orders/{id}/status")
async def update_order_status(id: int, status: str, db: AsyncSession = Depends(get_db)):
    """
    Обновляет статус заказа по ID.
    """
    order_service = OrderService(OrderDAO(db), ProductDAO(db))
    return await order_service.update_order_status(id, status)