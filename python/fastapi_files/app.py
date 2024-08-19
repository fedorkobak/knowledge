from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import Redis

def lifespan(_: FastAPI) -> None:
    redis = Redis.from_url("redis://localhost:6380")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

app = FastAPI(lifespan=lifespan)

from random import random

@app.get("/")
@cache(expire=60)
def index():
    return random()
