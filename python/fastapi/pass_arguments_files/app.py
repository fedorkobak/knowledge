from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    param1: int
    param2: str

app = FastAPI()

@app.post("/")
def read_json(item:Item):
    return f"""I have got:
    param1={item.param1};
    param2={item.param2}."""
