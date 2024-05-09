import logging
import logging.config
from fastapi import FastAPI, HTTPException

app = FastAPI()
logging.config.fileConfig("./app/uvicorn_logging.ini")

@app.get("/")
def handle():
    return "hello"
