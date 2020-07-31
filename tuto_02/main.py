from fastapi import FastAPI
from types import ModelName

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/float/{f_num}")
async def read_item(f_num: float):
    return {"float_num": f_num}

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    res = dict()
    res["model_name"] = model_name
    res["message"] = "Have some residuals"

    if model_name == ModelName.alexnet:
        res["message"] = "Deep Learning FTW!"

    elif model_name.value == "lenet":
        res["message"] = "LeCNN all the images"

    return res
