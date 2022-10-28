"""Partie fast API"""
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    val1: int
    val2: int
    res:  int = 0

app = FastAPI()

@app.post("/mult/")
async def create_item(item: Item):
    item.res = item.val1*item.val2
    return item


@app.get("/tablemulti/{Table}")
async def read_item(Table: int):
    result={
            "X1": Table*1,
            "X2": Table*2,
            "X3": Table*3,
            "X4": Table*4,
            "X5": Table*5,
            "X6": Table*6,
            "X7": Table*7,
            "X8": Table*8,
            "X9": Table*9,
            "X10": Table*10
        }
    return result



"""
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baaaaaaaaaz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit]
"""
"""
app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default='None', max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""

"""post et get """
""" vboxuser halo4"""