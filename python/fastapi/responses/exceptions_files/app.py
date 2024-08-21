from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class MyException(Exception):
    def __init__(self, message):
        self.message = message

app = FastAPI()

@app.exception_handler(MyException)
async def unicorn_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.message} did something."}
    )

@app.get("/")
def divide():
    raise MyException("My god")
