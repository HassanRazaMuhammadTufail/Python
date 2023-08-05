from typing import Union, Annotated, Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()

items = {
    1:{
        "name": "Item 1",
        "class": "new",
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
        if items[item_id]["name"] == name:
            return items[item_id]
        return {
            "Data": "Not found",
            "ord": ord(name),
            "chr": chr(97),
            "bytes": bytes("hassan")
        }