from fastapi import FastAPI

app = FastAPI()

@app.get("/ex1/{par1}{par2=10}{par3}{par4=10}")
def ex1(par1:int, par2:int, par3=10, par4=10):
    return "hello"

@app.get("/ex2")
def ex2(par1:int, par2=10):
    return "hello"
