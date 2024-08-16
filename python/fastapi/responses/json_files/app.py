from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get() -> str:
    return 'hello'
