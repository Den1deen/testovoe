from dao.product_dao import ProductDAO
from models.product import Product

class ProductService:
    def __init__(self, product_dao: ProductDAO):
        self.product_dao = product_dao

    async def create_product(self, product_data: dict) -> Product:
        product = Product(**product_data)
        return await self.product_dao.create_product(product)

    async def get_product(self, product_id: int) -> Product:
        return await self.product_dao.get_product(product_id)

    async def get_all_products(self) -> list[Product]:
        return await self.product_dao.get_all_products()

    async def update_product(self, product_id: int, product_data: dict) -> Product:
        return await self.product_dao.update_product(product_id, product_data)

    async def delete_product(self, product_id: int):
        await self.product_dao.delete_product(product_id)