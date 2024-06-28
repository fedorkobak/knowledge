
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Output(BaseModel):
    a : int
    b : str

@app.get("/")
def return_dict() -> Output:
    return Output(a=10, b="string value")
