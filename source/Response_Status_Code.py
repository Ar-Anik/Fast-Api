from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=202)
async def body1(name: str):
    return {
        "name": name
    }


# About HTTP status codes
@app.post("/status/", status_code=status.HTTP_201_CREATED)
async def body2(name: str):
    return {
        "name": name
    }

if __name__ == "__main__":
    unicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
