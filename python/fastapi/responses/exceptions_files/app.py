from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class MyException(Exception):
    def __init__(self, message):
        self.message = message

app = FastAPI()

@app.exception_handler(MyException)
def unicorn_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.message} did something."},
        headers={"key1": "10", "key2": "string value"}
    )

@app.get("/")
def divide():
    raise MyException("My god")
