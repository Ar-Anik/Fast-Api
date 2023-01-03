import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
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


# Nested Models
class Image1(BaseModel):
    url: str
    img_name: str


class Image2(BaseModel):
    url: HttpUrl
    img_name: str


class userInfo1(BaseModel):
    name: str
    age: float = None
    gender : str
    image: Image1 = None


class userInfo2(BaseModel):
    name: str
    age: float = None
    gender: str
    image: Image2 = None


class userInfo3(BaseModel):
    name: str
    age: float = None
    gender: str
    image: List[Image2] = None


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

# {
#     "name": "anik",
#     "age": 14.3,
#     "gender": "Male",
#     "image": {
#         "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#         "img_name": "mia khalifa"
#     }
# }

@app.post("/nested2/{nested_id}")
async def body6(nested_id: int, user: userInfo2):
    result = {
        "nested_id": nested_id,
        "user": user
    }

    return result


# {
#     "name": "anik",
#     "age": 14.3,
#     "gender": "Male",
#     "image": [
#         {
#             "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#             "img_name": "mia khalifa"
#         },
#         {
#             "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#             "img_name": "mia khalifa"
#         }
#     ]
# }

@app.post("/nested3/{nested_id}")
async def body7(nested_id: int, user: userInfo3):
    result = {
        "nested_id": nested_id,
        "user": user
    }

    return result


# Deeply Nested Models

class userInfo(BaseModel):
    name: str
    description: str = None
    price: float
    employee: List[userInfo3]


# {
#     "name": "a-it",
#     "description": "it is a good it frame in bangladesh",
#     "price": 20000000000.78,
#     "employee": [
#         {
#             "name": "anik",
#             "age": 14.3,
#             "gender": "Male",
#             "image": [
#             {
#                 "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#                 "img_name": "mia khalifa"
#             },
#             {
#                 "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#                 "img_name": "mia khalifa"
#             }
#           ]
#         },
#         {
#             "name": "anik",
#             "age": 14.3,
#             "gender": "Male",
#             "image": [
#             {
#                 "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#                 "img_name": "mia khalifa"
#             },
#             {
#                 "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0gCWDpc-k7ETm_F7VFx9YntCVgiJy1cqYA&usqp=CAU",
#                 "img_name": "mia khalifa"
#             }
#           ]
#         }
#     ]
# }


# List Body

@app.post("/deeply/{nested_id}")
async def body8(nested_id: int, employees: userInfo):
    return {
        "nested_id": nested_id,
        "employeeList": employees
    }


# Body of pure lists

# http://localhost:9000/images/multiple
# [
#   {
#     "url": "https://beritabaru.co/wp-content/uploads/2019/12/58046fa81db81.jpg",
#     "img_name": "mia_khalifa"
#   },
#   {
#     "url": "https://beritabaru.co/wp-content/uploads/2019/12/58046fa81db81.jpg",
#     "img_name": "mia_khalifa"
#   },
#   {
#     "url": "https://beritabaru.co/wp-content/uploads/2019/12/58046fa81db81.jpg",
#     "img_name": "mia_khalifa"
#   },
#   {
#     "url": "https://beritabaru.co/wp-content/uploads/2019/12/58046fa81db81.jpg",
#     "img_name": "mia_khalifa"
#   },
#   {
#     "url": "https://beritabaru.co/wp-content/uploads/2019/12/58046fa81db81.jpg",
#     "img_name": "mia_khalifa"
#   }
# ]

@app.post("/images/multiple")
async def create_multiple_images(images: List[Image2]):
    return images


# @app.post("/index-weights/")
# async def create_index_weights(weights: dict[int, float]):
#     return weights


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")));
