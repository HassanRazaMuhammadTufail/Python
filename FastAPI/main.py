from typing import Union, Annotated

from fastapi import FastAPI, Path

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
def read_item(item_id: int = Path(title="The ID of the item to get", gt = 0)):
    return items[item_id]
