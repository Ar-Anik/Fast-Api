from fastapi import FastAPI
from fastapi import Query
import uvico

app = FastAPI(debug=True)

@app.get("/items")
async def read_items(query: str = None):
    result = {"user":[
        {
            "user-1" : "Aubdur Rob Anik",
            "user-1-id" : 1
        },
        {
            "user-2" : "Osim Akram",
            "user-2-id" : 2
        }
    ]}

    if query:
        result.update({"query" : query})

    return result

# Query Range Maximum Length
# http://127.0.0.1:8000/model/?query=aubdur rob

@app.get("/model/")
async def model_item(query: str = Query(default=None, max_length=10)):
    result = {
        "items" : [
            {
                "model_name" : "Sunny",
                "age" : 35
            },
            {
                "model_name" : "Jordi",
                "age" : 24
            }
        ]
    }
    if query:
        result.update({"query": query})

    return result

# Query Range Minimum and Maximum


if "__name__" == "__main__":
    uvicorn.run(app, host="12.0.0.1", port=8000)
