import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug=True)

class Item(BaseModel):
    name: str
    type: str=None
    income: float
    tax: float=None

@app.post("/{user_id}")
async def create(user_id: int, user:Item, price:float=None, extra: int=None):
    result = {"id":user_id, **user.dict()}

    if price:
        result.update({"Price": price+extra})

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('9000')))
