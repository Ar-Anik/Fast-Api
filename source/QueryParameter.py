# Query Parameter are a defined set of parameters attached to the end of a url.
# They are extensions of the URL.
# Used to help define specific content or actions based on the data being passed.
# A query parameter is the set of key-value pairs that go after the ? in a URL, separated by & characters.

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# query Parameter with by default value
# http://127.0.0.1:8000/item/?value1=10&value2=20
# http://127.0.0.1:8000/item/?value1=10

@app.get("/item/")
async def default_value(value1: int = 0, value2: int = 10):
    return {"Value-1 " : value1, "Value-2 " : value2}

# Optional Query Parameter
# http://127.0.0.1:8000/user/?user_name=%22Aubdur%20Rob%20Anik%22&user_id=6

@app.get("/user/")
async def optional_parameter(user_name: str = "anik", user_id: int = None):
    if user_id:
        return {
            "User Name " : user_name,
            "User Id " : user_id
        }
    return {"User Name " : user_name}

# required Query Parameter
# http://127.0.0.1:8000/model/sunny/?rate=100000

@app.get("/model/{model_name}")
async def required_parameter(model_name: str, rate: str = None):
    if rate:
        return {
            "Model Name" : model_name,
            "Rate" : rate
        }
    return {"Model Name" : model_name}

# Query Parameter as Boolean Value
# http://127.0.0.1:8000/boolean/?value=True
# http://127.0.0.1:8000/boolean/?value=1
# http://127.0.0.1:8000/boolean/?value=on
# http://127.0.0.1:8000/boolean/?value=off

@app.get("/boolean/")
async def bool_value(value: bool = True):
    return {"Value " : value}


if "__name__" == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

