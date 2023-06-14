from fastapi import FastAPI,request


app = FastAPI()


@app.get("/add/")
def add(num1: float, num2: float):
    return {"the add of two num is": num1 + num2}


@app.get("/sub/")
def sub(num1: float, num2: float):
    return {"the sub of two num is": num1 - num2}


@app.get("/mul/")
def mul(num1: float, num2: float):
    return {"the multiplication of two num is": num1 * num2}


@app.get("/div/")
def div(num1: float, num2: float):
    try:
        return {"The division of two num is": num1 / num2}
    except Exception as e:
        print(e)


@app.put("/division_update/")
def div_up(num1: float, num2: float):
    return{"updated division value is": num1 / num2}


@app.post("/add/")
def addition():

    a = request.body


