from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Config

# Создаем асинхронный движок базы данных
DATABASE_URL = Config.DATABASE_URL
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем сессию
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Функция для получения сессии в зависимости
async def get_db():
    async with async_session() as session:
        yield session