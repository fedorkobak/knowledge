from fastapi import FastAPI

app = FastAPI()

@app.get("/{required}{no}")
def say_hello(required : int, no=10):
    return "hello"
