import uvicorn
from fastapi import FastAPI, Form

app = FastAPI(debug=True)

@app.post("/login/")
async def login(username: str = Form(default=None), password: str = Form(default=None)):
    return {
        "username": username,
        "password": password
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
