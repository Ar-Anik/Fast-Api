from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(debug=True)

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host

    return {
        "Client_host": client_host,
        "item_id": item_id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
