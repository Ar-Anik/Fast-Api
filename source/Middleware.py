import uvicorn
import time
from fastapi import FastAPI, Request

app = FastAPI(debug=True)

@app.middleware('http')
async def add_process_time_heads(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time;

    response.headers["X-Process-Time"] = str(process_time)

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
