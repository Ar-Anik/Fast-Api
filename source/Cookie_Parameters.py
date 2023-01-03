import uvicorn
from fastapi import FastAPI, Cookie, Request

app = FastAPI(debug=True)

# curl -X GET "http://127.0.0.1:9000/items/" -H  "accept: application/json" -H  "Cookie: ads_id=foobar"

@app.get("/items/")
async def read_items(ads_id: str = Cookie(default=None)):
    print("ads_id", request.cookies)
    return {
        "ads_id": ads_id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
