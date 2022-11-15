from fastapi import FastAPI
from enum import Enum
import uvicorn

app = FastAPI(debug = True)

# Path with id
@app.get("/items/{item_id}")
async def function_with_id(item_id):
    return {"item_id" : item_id};

# Path with fix data type
@app.get("/data/{data_type}")
async def function_with_integer_data_type(data_type : int) :
    return {"item_id" : data_type}

# Fixed Vs Modify
# Order is Matter

@app.get("/user/me")
async def function_with_url():
    return {"Name ": "Aubdur Rob Anik"}

@app.get("/user/{user_name}")
async def function_with_modify_url(user_name: str):
    return {"User Name ": user_name}

# Path Parameter Declare By Enum

class ModelName(str, Enum):
    ml = "machine_learning"
    dl = "deep_learning"
    ds = "data_science"
    tm = "transformer_model"

@app.get("/python/{name}")
async def get_with_enum(name : ModelName):        #input name only in ModelName otherwise error (path parameter : function parameter)
    if name == ModelName.ml:
        return {
            "model name " : name,
            "Full Name " : ModelName.ml
        }

    elif name == ModelName.dl:
        return {"mode name " : name, "Full Name " : ModelName.dl}

    elif name is ModelName.tm:
        return {
            "Model Name" : name,
            "Full Name" : ModelName.tm
        }

    return {"mode name " : name, "Full Name " : ModelName.ds}

# With Path Parameter
@app.get("/model/{file_path:path}")
async def function_path_parameter(file_path):
    return {
        "File Path" : file_path
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 8000)
