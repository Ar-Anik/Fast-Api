import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Literal

app = FastAPI(debug=True)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

# Return the same input data
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user

# Add an Output model

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

@app.post("/usr/", response_model=UserOut)
async def body1(user: UserIn):
    return user

# Response Model encoding parameters

class rItem(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.3},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=rItem, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

@app.get("/literal/{item_id}", response_model=rItem, response_model_exclude_unset=True)
async def read_item(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]


# response_model_include and response_model_exclude

@app.get("/include/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
async def body2(item_id: str):
    return items[item_id]

@app.get("/exclude/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def body3(item_id: str):
    return items[item_id]


# response_model_include and response_model_exclude by Using lists instead of sets
@app.get("/lst/{item_id}/name", response_model=Item, response_model_include=["name", "description"])
async def body4(item_id: str):
    return items[item_id]

@app.get("/lst/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def body5(item_id):
    return items[item_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
