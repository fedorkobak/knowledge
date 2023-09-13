from fastapi import FastAPI

app = FastAPI()

@app.get("/divide")
def divide(a:int, b:int) -> int:
    return a/b