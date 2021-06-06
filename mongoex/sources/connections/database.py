from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    client: AsyncIOMotorClient = None


db = Database()
db_name = 'fastapi'


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def on_startup():
    db.client = AsyncIOMotorClient("localhost", 27017)


async def on_shutdown():
    db.client.close()
