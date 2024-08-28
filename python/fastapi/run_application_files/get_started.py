from fastapi import FastAPI

my_first_app = FastAPI()

@my_first_app.get("/")
def index(a: int, b: str):
    return f"a = {a}, b = {b}"
