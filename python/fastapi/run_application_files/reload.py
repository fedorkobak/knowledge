from fastapi import FastAPI

my_first_app = FastAPI()

@my_first_app.get("/")
def say_hello():
    return "updated line"
