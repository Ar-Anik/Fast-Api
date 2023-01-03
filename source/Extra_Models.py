import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union, List, Dict

app = FastAPI(debug=True)

# Multiple Models
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str = None

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    # user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User Saved! .. not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def body1(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


# Reduce Duplication
class rdUserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

class rdUserIn(rdUserBase):
    password: str

class rdUserOut(rdUserBase):
    pass

class rdUserInDB(rdUserBase):
    hashed_password: str

def rdFake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def rdFake_save_user(user_in: rdUserIn):
    hashed_password = rdFake_password_hasher(user_in.password)
    user_in_db = rdUserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User Saved! ..not really")
    return user_in_db

@app.post("/usr/", response_model=rdUserOut)
async def body2(user_in: rdUserIn):
    user_saved = rdFake_save_user(user_in)
    return user_saved

# Union or anyOf
class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = "Car"
    price: float = None

class PlaneItem(BaseItem):
    type = "Plane"
    seatCount: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {"description": "Music is my aeroplane it's my aeroplane", "type": "plane", "size": 5}
}

@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def body3(item_id: str):
    return items[item_id]

# List of models
class Item(BaseModel):
    name: str
    description: str

items = [
    {"name": "Foo", "description": "There born a hero"},
    {"name": "Red", "description": "It's my aeroplane"},
    {"name": "White Angle", "description": "It's a star"}
]

@app.get("/items/", response_model=List[Item])
async def body4():
    return items

# Response with arbitary dict
@app.get("/keyword-weights/", response_model=Dict[str, float])
async def body5():
    return {
        "Foo": 2.3,
        "Bar": 3.4,
        "Baz": 5.9
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
