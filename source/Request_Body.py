# Pydantic is a Python library for data modeling/parsing that has efficient error handling and a custom validation mechanism

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug=True)

# Request Body or Data Model
class Item(BaseModel):
    name: str
    type: str = None
    income: float
    tax: float = None

@app.post("/itms")
async def create_itm(itm: Item):
    return itm

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        total = item.income - item.tax
        item_dict.update({"TotalIncome" : total})
    return item_dict

# Request body + path Parameter
# Update replacing with PUT, PUT is used to receive data that should replace the existing data.

@app.put("/items/{item_id}")
async def create_item_with_id(item_id: int, item: Item):
    return {"item_id" : item_id, **item.dict()}

# Request body + path + query parameters
# http://127.0.0.1:8000/model/sunny/?price=1000

@app.post("/model/{model_name}")
async def create_model(model_name: str, item:Item, price: float = None):
    result = {"model_name" : model_name, **item.dict()}

    if price:
        result.update({"Price": price})

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
