from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/")
def return_dict():
    raise HTTPException(404, "Custom not found")
