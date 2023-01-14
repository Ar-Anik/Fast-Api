import uvicorn
from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List

app = FastAPI(debug=True)

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

    return fake_db[id]

# Using Pydantic's exclude_unset parameter

class Model(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/show/items/{item_id}", response_model=Model)
async def body1(item_id: str):
    return items[item_id]

@app.patch("/update/items/{item_id}", response_model=Model)
async def body2(item_id: str, item: Model):
    stored_item_data = items[item_id]

    stored_item_model = Model(**stored_item_data)

    update_data = item.dict(exclude_unset=True)

    update_itm = stored_item_model.copy(update=update_data)

    items[item_id] = jsonable_encoder(update_itm)

    return update_itm

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
