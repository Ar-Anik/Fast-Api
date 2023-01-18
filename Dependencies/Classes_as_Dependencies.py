from fastapi import Depends, FastAPI

app = FastAPI(debug=True)

fake_items_db = [
    {
        "item_name": "Foo"
    },
    {
        "item_name": "Bar"
    },
    {
        "item_name": "Baz"
    }
]

class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 200):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def body1(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}

    if commons.q:
        response.update({
            "q": commons.q
        })

    items = fake_items_db[commons.skip]
    response.update({"items": items})

    return response

@app.get("/class/items/")
async def body2(commons=Depends(CommonQueryParams)):
    response = {}

    if commons.q:
        response.update({
            "q": commons.q
        })

    items = fake_items_db[commons.skip]
    response.update({"items": items})

    return response

@app.get("/cls/items/")
async def body3(commons: CommonQueryParams=Depends()):
    response = {}

    if commons.q:
        response.update({
            "q": commons.q
        })

    items = fake_items_db[commons.skip]
    response.update({"items": items})

    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
