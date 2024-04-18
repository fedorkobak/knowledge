from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/{is_ok}")
def say_hello(is_ok : bool):
    if is_ok:
        return "im fine"
    else:
        raise HTTPException(status_code=404, detail="Item not found")
