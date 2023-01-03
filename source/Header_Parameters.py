import uvicorn
from fastapi import FastAPI, Header
from typing import List

app = FastAPI(debug=True)

@app.get("/items/")
async def body(user_agent: str = Header(default=None)):
    return {
        "user-Agent": user_agent,
    }

@app.get("/itms/")
async def body1(strange_header: str = Header(default=None, convert_underscores=False)):
    return {
        "strange_header": strange_header
    }


@app.get("/duplic/")
async def body2(x_token: List[str] = Header(default=None)):
    return {
        "X-token": x_token
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
