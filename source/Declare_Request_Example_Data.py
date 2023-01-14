import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI(debug=True)

# Pydantic schema_extra
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}

    return results


# Field Additional Arguments
class FieldItem(BaseModel):
    name: str = Field(example="Aluu")
    description: str = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float = Field(default=None, example=3.2)


@app.post("/field/{item_id}")
async def update_item(item_id: int, item: FieldItem):
    results = {
        "item_id": item_id,
        "item": item
    }

    return results


# example in OpenAPI

class exampleItem(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.put("/example/{item_id}")
async def update_item(
        item_id: int,
        item: exampleItem = Body(
            default=...,
            example={
                "name": "mou",
                "description": "A very nice Item",
                "price": 35.6,
                "tax": 3.2
            }
        )
):
    result = {"item_id": item_id, "item": item}

    return result


# examples in OpenAPI
class examplesItem(BaseModel):
    name: str
    occupation: str = None
    salary: float
    tax: float = None

@app.post("/examples/{item_id}")
async def update_item(
        item_id: int,
        item: examplesItem = Body(
            examples= {
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "anik",
                        "occupation": "SE",
                        "salary": 19.5,
                        "tax": 0.15
                    }
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price strings to actual numbers automatically",
                    "value": {
                        "name": "oni",
                        "salary": 25.55,
                    }
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Das",
                        "salary": 30.31
                    }
                }
            },
            default=...
        )
):
    results = {"item_id": item_id, "item": item}

    return results


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



