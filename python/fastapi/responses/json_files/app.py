from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get() -> JSONResponse:
    return JSONResponse(
        content={"key": "value"}, 
        status_code=255, 
        headers={"name": "Fedor", "surname": "Kobak"}
    )
