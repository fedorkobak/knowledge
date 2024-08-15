import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hello():
    return "I'm started from __main__"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
