"""Partie fast API"""
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Union
import aioredis



app = FastAPI()


@app.get("/tablemulti/{Table}")
async def read_item(Table: int):
    redis = aioredis.from_url("redis://redis:6379")
    if (await redis.get("my-key")) :
        value = await redis.get("my-key")
        value = int(value)
        value = value + 1
        await redis.set("my-key", value)
        return value
    else :
        await redis.set("my-key", 0)
        value = await redis.get("my-key")
        return value
"""
@app.get("/tablemulti/{Table}")
async def read_item(Table: int):
    redis = aioredis.from_url("redis://localhost")
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
"""

