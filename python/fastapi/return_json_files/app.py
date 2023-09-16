from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def json_as_answer():
    return {
        "key1" : "value1",
        "key2" : "value2",
        6 : 34
    }
