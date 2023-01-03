import uvicorn
from fastapi import FastAPI
from fastapi import Query, Path
from pydantic import Required

app = FastAPI(debug=True)

# path parameter
# localhost:9000/user/anik/?query=Aubdur Rob
@app.get("/user/{user_name}")
async def read(user_name: str = Path(default=Required, min_length=3, max_length=10), query:str = Query(default=None, min_length=4, max_length=12)):
    result = {"User Name" : user_name}

    if query:
        result.update({"query": query})

    return result

# detect the parameters by their names, types and default declarations (Query, Path, etc),
# it doesn't care about the order.
@app.get("/items/{item_name}/")
async def read2(query:str, item_name: str = Path(default=Required, max_length=20)):
    result = {
        "item_name": item_name,
        "query": query
    }

    return result

# # Not work because Path function use End of the function argument
# @app.get("/itemsss/{item_id}")
# async def read_items(item_id: int = Path(..., title="The ID of the item to get"), q:str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# # Order the parameters by *
@app.get("/order/{item_name}")
async def read3(*, item_name: str = Path(default=..., max_length=20), query: str):
    result = {
        "item_name": item_name,
        "query": query
    }

    return result

# ge: greater than or equal
# gt: greater than
# le: less than or equal
# lt : less than
@app.get("/number/{ids}")
async def read4(ids: int = Path(default=Required, ge=5, le=15), query: int = Query(default=None, gt=10, lt=20)):
    result = {"Id": ids}

    if query:
        result.update({"query": query})

    return result

# Number validations: floats, greater than and less than
@app.get("/nmbr/{ids}")
async def read5(ids: float = Path(default=..., gt=1.8, lt=6.5), query: float = Query(default=None, gt=2.4, lt=8.3)):
    result = {"ids": ids}

    if query:
        result.update({"query": query})

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
