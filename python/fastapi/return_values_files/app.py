from fastapi import FastAPI

app = FastAPI()

@app.get("/dict")
def return_dict():
    return {
        "key1" : "value1",
        "key2" : "value2",
        6 : 34
    }

@app.get("/list")
def return_json():
    return [1, 2, 3, "hello", True]
