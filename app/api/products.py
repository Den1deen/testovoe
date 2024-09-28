from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.product_service import ProductService
from dao.product_dao import ProductDAO
from database import get_db
from schemas.product_schema import ProductCreate, ProductOut

router = APIRouter()

@router.post("/products/", response_model=ProductOut)
async def create_product(product_data: ProductCreate, db: AsyncSession = Depends(get_db)):
    """
    Создает новый продукт на складе.
    """
    product_service = ProductService(ProductDAO(db))
    return await product_service.create_product(product_data.dict())

@router.get("/products/", response_model=list[ProductOut])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    """
    Возвращает список всех продуктов на складе.
    """
    product_service = ProductService(ProductDAO(db))
    return await product_service.get_all_products()

@router.get("/products/{id}", response_model=ProductOut)
async def get_product(id: int, db: AsyncSession = Depends(get_db)):
    """
    Возвращает информацию о продукте по ID.
    """
    product_service = ProductService(ProductDAO(db))
    product = await product_service.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{id}", response_model=ProductOut)
async def update_product(id: int, product_data: ProductCreate, db: AsyncSession = Depends(get_db)):
    """
    Обновляет информацию о продукте по ID.
    """
    product_service = ProductService(ProductDAO(db))
    product = await product_service.update_product(id, product_data.dict())
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{id}")
async def delete_product(id: int, db: AsyncSession = Depends(get_db)):
    """
    Удаляет продукт по ID.
    """
    product_service = ProductService(ProductDAO(db))
    await product_service.delete_product(id)
    return {"detail": "Product deleted"}