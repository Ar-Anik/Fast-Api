from fastapi import Cookie, Depends, FastAPI
import uvicorn

app = FastAPI()

def query_extractor(q: str = None):
    return q

def query_or_cookie_extractor(q: str=Depends(query_extractor), last_query: str=Cookie(default=None)):
    print("Q: ", q)
    print("last_query: ", last_query)

    if not q:
        return last_query
    return q

@app.get("/items/")
async def read_query(query: str = Depends(query_or_cookie_extractor)):
    return {
        "query": query
    }

@app.get("/dependencies/items")
async def needy_dependency(fresh_value: str = Depends(query_or_cookie_extractor, use_cache=False)):
    return {
        "fresh_value": fresh_value
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
