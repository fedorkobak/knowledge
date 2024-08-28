from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def index(request: Request):
    return request.client.host
