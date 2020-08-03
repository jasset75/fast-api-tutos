from fastapi import FastAPI
from tuto_02.main_types import ModelName
from tuto_02.fake_db import fake_items_db
from typing import Optional

app = FastAPI()


@app.get("/")
async def welcome():
    return {"welcome": "To have here or take away?. Don't forget the cutlery!"}


@app.get("/items/")
async def read_item_params(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip+limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    item = {"item": None}
    if item_id < len(fake_items_db):
        item = fake_items_db[item_id]

    if q:
        item.update({"q": q})

    return item


@app.get("/float/{f_num}")
async def read_float(f_num: float):
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


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
