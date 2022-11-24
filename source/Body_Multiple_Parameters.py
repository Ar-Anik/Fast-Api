import uvicorn
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Required

app = FastAPI(debug=True)

class Person(BaseModel):
    name : str
    age : int = None
    salary: float
    position: str = None

class User(BaseModel):
    fast_name : str
    last_name: str = None
    user_id : str

@app.post("/items/{item_id}")
async def update_item(*, item_id: int = Path(default=..., gt=0, lt=101), q: str=None, person: Person = None):
    result = {
        "item_id" : item_id,
    }

    if q:
        result.update({"q": q})

    result.update({"person": person})

    return result


@app.post("/user/{user_type}")
async def update_user(*, user_type: str=Path(default=Required, min_length=5, max_length=15), query: str=Query(default=None, min_length=5, max_length=18), person:Person, user_info:User):
    result = {
        "person" : person,
        "user" : user_info,
        "user_type": user_type,
    }

    if query:
        result.update({"query": query})

    return result

# Singular values in body
# http://localhost:9000/body/6
# {
#   "person": {
#     "name" : "Anik",
#     "age" : 14,
#     "salary" : 30.80,
#     "position" : "Junior Software Engineer"
#   },
#   "user": {
#     "fast_name" : "Aubdur Rob",
#     "last_name" : "Anik",
#     "user_id" : "18101073"
#   },
#   "important": 10
# }

@app.post("/body/{ids}")
async def body_add(ids: int, person: Person, user: User, important: int=Body(default=Required, gt=5, lt=12)):
    result = {
        "ids": ids,
        "person": person,
        "user": user,
        "important": important
    }

    return result

@app.post("/multiplebody/{ids}")
async def bodys(*, ids: int, person: Person, user: User, extra: str=Body(default=Required), query: str):
    result = {
        "body_id": ids,
        "person": person,
        "user": user,
        "extra": extra,
        "query": query
    }

    return result

# embed=True
@app.post("/embed/")
async def body(person: Person = Body(default=Required, embed=True)):
    result = {"Person": person}

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

