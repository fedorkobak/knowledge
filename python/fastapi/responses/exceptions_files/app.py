from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/")
def index():
    raise HTTPException(
        status_code=400, 
        detail="Test value",
        headers={"key": "value"}
    )
