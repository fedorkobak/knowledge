from fastapi import FastAPI

my_first_app = FastAPI()

@my_first_app.get("/")
def get_dict():
    return {"a": "value", "b": 32}
