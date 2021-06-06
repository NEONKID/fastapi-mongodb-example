from abc import ABCMeta
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import final

from mongoex.sources.connections.database import db_name


class BaseService(metaclass=ABCMeta):
    def __init__(self, collection_name: str, db: AsyncIOMotorClient) -> None:
        self._collection = db[db_name][collection_name]

    @final
    async def delete_by_id(self, item_id: str):
        row = await self._collection.delete_one({"_id": ObjectId(item_id)})
        if not row:
            # raise error 404
            return None

    @final
    async def find_all(self):
        cursor = self._collection.find()
        results = list(map(lambda item: item, await cursor.to_list(length=100)))

        return results

    @final
    async def find_by_id(self, item_id: str):
        # Todo: Error catching 대한 로직 구상 필요
        row = await self._collection.find_one({"_id": ObjectId(item_id)})
        if not row:
            # raise error 404
            return None

        return row

    @final
    async def save(self, req: dict):
        return await self._collection.insert_one(req)

    @final
    async def update(self, item_id: str, req: dict):
        await self._collection.update_one({"_id": ObjectId(item_id)}, {"$set": req})
        return await self.find_by_id(item_id)
