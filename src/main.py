from fastapi import FastAPI
from routers import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

app = FastAPI()

@app.on_event("startup")
async def start_db_client():
    settings=get_settings()
    app.mongo_conn=AsyncIOMotorClient(settings.MONGO_URL)
    app.db_client=app.mongo_conn(settings.MONGO_DATABASE)

app.on_event("shutdown")
async def shutdown_df_client():
    app.mongo_conn.close()

app.include_router(base.base_router)
app.include_router(data.data_router)

