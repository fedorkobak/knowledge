from random import random

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

redis = aioredis.from_url("redis://localhost:6380")
FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

app = FastAPI()

@app.get("/")
@cache(expire=600)
def index():
    data = {"detail": str(random())}
    return JSONResponse(content=data, status_code=500)
