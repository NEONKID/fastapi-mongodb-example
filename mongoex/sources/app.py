from fastapi import FastAPI

from mongoex.sources.api.memo import router_memo
from mongoex.sources.connections import database


def create_app():
    mongodb_app = FastAPI()

    mongodb_app.include_router(router_memo)

    @mongodb_app.on_event("startup")
    async def on_startup():
        await database.on_startup()

    @mongodb_app.on_event("shutdown")
    async def on_shutdown():
        await database.on_shutdown()

    return mongodb_app
