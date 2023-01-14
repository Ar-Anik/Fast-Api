import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI(debug=True)

items = {
    "computer": "I have a computer",
    "latlop": "This is very expensive",
    "bag": "Bag is very chep"
}

@app.get("/items/{item_id}")
async def body1(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item Not Found")

    return {
        "item": items[item_id]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

# Add custom headers

@app.get("/items-header/{item_id}")
async def body2(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not Found", headers={"X-Error": "There Goes My Error"})

    return {
        "item": items[item_id]
    }

# custom exception handlers

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=404, content={
        "message": f"OOPS! {exc.name} did something. There goes a rinbow...."
    })

@app.get("/unicorn/{name}")
async def body3(name: str):
    if name == "yolo":
        raise UnicornException(name=name)

    return {
        "unicorn_name": name
    }

# Override the default exception handlers

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/override/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")

    return {
        "item_id": item_id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
