from fastapi import FastAPI

app = FastAPI()

@app.get("/divide/{a}/{b}")
def divide(a:int, b:int) -> float:
    return a/b
