import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("9000"))


