import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Set

app = FastAPI(debug=True)

class Item(BaseModel):
    name : str
    weight: int = None
    price : float
    tax : float = None
    description : str = None
    tags: list = []


class Person1(BaseModel):
    name: str
    age: float = None
    gender: str
    qualification: List[str] = []

class Person2(BaseModel):
    name: str
    age: float = None
    gender: str
    number: List[float] = []

# Duplicate Not Allowed
class Info(BaseModel):
    name: str
    age: float = None
    gender: str
    fibonacci: Set[str] = []

#Nested Models
class Image1(BaseModel):
    url: str
    img_name: str

class userInfo1(BaseModel):
    name: str
    age: float = None
    gender : str
    image: Image1 = None


# List fields
@app.post("/item/{item_id}")
async def body1(item_id:int, items:Item):
    result = {
        "item_id": item_id,
        "item" : items
    }

    return result

# List fields with type parameter
@app.post("/user/{user_id}")
async def body2(user_id:int, person: Person1):
    result = {
        "user_id": user_id,
        "Person": person
    }

    return result

@app.put("/usr/{usr_id}")
async def body3(usr_id: int, person: Person2):
    result = {
        "user_id": usr_id,
        "person": person
    }

    return result

@app.put("/set/{set_id}")
async def body4(set_id: int, set_info: Info):
    result = {
        "set-id": set_id,
        "Info": set_info
    }

    return result

# Nested Models
@app.post("/nested/{nested_id}")
async def body5(nested_id: int, user: userInfo1):
    result = {
        "nested_id": nested_id,
        "user": user
    }

    return result




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")));
