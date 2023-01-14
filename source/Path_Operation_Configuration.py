from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Set
from enum import Enum

app = FastAPI(debug=True)

# Response Status Code

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def body1(item: Item):
    return item

# Tags

@app.post('/tags/items/', response_model=Item, tags=["items"])
async def body2(item: Item):
    return item

@app.get("/tags/item/", tags=["items"])
async def body3():
    return [{
        "Name": "Foo",
        "Price": 42
    }]

@app.get("/tags/users/", tags=["users"])
async def body4():
    return [
        {
            "username": "anik"
        }
    ]

# Tags with Enums

class Tags(Enum):
    items = "items",
    users = "users"

@app.get("/enum/items/", tags=[Tags.items])
async def body5():
    return ["Portal Gun", "Plumbus"]

@app.get("/enum/users/", tags=[Tags.users])
async def body6():
    return ["Rick", "Morty"]

# Summary and description

@app.post(
    "/summary/items/",
    response_model=Item,
    summary="Create an Item",
    description="Create an Item with all the information, name, description, price, tax and a set of unique tags"
)
async def body7(item: Item):
    return item

# Description from docstring
@app.post("/docstring/items/", response_model=Item, summary="Create an Item")
async def body8(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """

    return item

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
