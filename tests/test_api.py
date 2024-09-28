import pytest

from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/products/", json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 100.0,
            "quantity": 10
        })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"