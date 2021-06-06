from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from mongoex.sources.connections.database import get_database
from mongoex.sources.dao import BaseService


class MemoService(BaseService):
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)) -> None:
        super().__init__('memo', db)
