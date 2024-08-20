from random import random
from collections.abc import AsyncIterator

from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost:6380")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
@cache(expire=600)
def index(id: int):
    return random()
