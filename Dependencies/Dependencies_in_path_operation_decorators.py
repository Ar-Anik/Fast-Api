from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import Required
import uvicorn

app = FastAPI(debug=True)

async def verify_token(x_token: str=Header(default=Required)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header(default=Required)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-key header invalid")

    return x_key

@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [
        {
            "item": "Foo"
        },
        {
            "item": "Bar"
        },
        {
            "item": "Baz"
        }
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
