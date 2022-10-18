from fastapi import FastAPI
import uvicorn

app = FastAPI(debug = True)

# A simple hello world API. It uses the get method. / indicates the root, however this doesn't have any reason why the method is named root.
# The method name can be anything.

@app.get("/")
async def root():
    return {"message" : "Hello world"}

@app.get("/home")
async def myhome():
    return {"message" : "This is come from home function"}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
