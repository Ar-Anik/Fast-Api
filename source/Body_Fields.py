import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, Required

app = FastAPI(debug=True)

class Person(BaseModel):
    name: str
    age : int = Field(default=Required, gt=0, lt=100)
    pid: str = Field(default=None, min_length=4, max_length=15)
    pemail: str = Field(default=..., description="This Field must be contained @ sign")

@app.post("/field/")
async def body1(person: Person = Body(default=Required, embed=True)):
    return person

# @app.post("/extra/")
# async def body2(person: Person = Body(default=None, embed=True), pcg: float = Field(default=Required)):
#     result = {"pcg": pcg}
#
#     if person:
#         result.update({"Person": person})
#
#     return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

