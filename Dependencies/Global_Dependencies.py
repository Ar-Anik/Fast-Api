from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import Required
import uvicorn

async def verify_token(x_token: str = Header(default=Required)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token Header Invalid")

async def verify_key(x_key: str = Header(default=Required)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key Header Invalid")

    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app.get("/items/")
async def read_items():
    return [
        {
            "item": "Portal Gun"
        },
        {
            "item": "Plumbus"
        }
    ]

@app.get("/users/")
async def read_users():
    return [
        {
            "username": "Rick"
        },
        {
            "username": "Morty"
        }
    ]

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
