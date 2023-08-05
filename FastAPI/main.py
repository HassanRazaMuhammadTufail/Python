from typing import Union, Annotated, Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    category: str
    price: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[int] = None

items = {
    1:{
        "name": "Item 1",
        "category": "new",
        "price": 10
    }
}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(title="The ID of the item to get", gt = 0, lt=2)):
    return items[item_id]

@app.get("/get-by-name/{item_id}")
def get_item_by_name(*, 
                     item_id: int = None,
                     name: Optional[str] = None,
                    #    = Query(title="The Name of the item to get"), 
                     test: int):
    for item_id in items:
        if items[item_id].name == name:
            return items[item_id]
        return {
            "Data": "Not found",
            "ord": ord(name),
            "chr": chr(97),
            "bytes": bytes("hassan")
        }

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"Error": "Item already exists."}
    items[item_id] = item
    return items

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {"Error": "Item Not Found."}
    
    if item.name != None:
        items[item_id]["name"] = item.name

    if item.category != None:
        items[item_id]["category"] = item.category

    if item.price != None:
        items[item_id]["price"] = item.price

    return items[item_id]
    
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"Error": "Item Not Found."}
    del items[item_id]
    return items