import uvicorn
from fastapi import FastAPI
from fastapi import Query
from pydantic import Required
from typing import List

app = FastAPI(debug=True)

@app.get("/model/")
async def read1(query: str=Query(default=None, max_length=10)):
    result = {
        "user" : [
            {
                "user-1": "Aubdur Rob Anik",
                "user-1-id": 1
            },
            {
                "user-2": "Anik Das",
                "user-2-id": 2
            }
        ]
    }

    if query:
        result.update({"query": query})

    return result

@app.get("/user/")
async def read2(query: str=Query(default=None, min_length=3, max_length=10)):
    result={
        "user": [
            {
                "user-1": "Mirza Shakil",
                "user-1-id": 1
            },
            {
                "user-2": "Imran Nazir Emon",
                "user-2-id": 2
            }
        ]
    }

    if query:
        result.update({"query":query})

    return result

# A regular expression is a sequence of characters that specifies a search pattern in text.
# Usually such patterns are used by string-searching algorithms for "find" or "find and replace"
# operations on strings, or for input validation
# regular expressions
# http://localhost:9000/items/?query=anik
@app.get("/items/")
async def read3(query: str=Query(default=None, regex="^anik$")):
    result = {
        "info" : {
            "name": "Anisul Islam Oni",
            "id": "18101073"
        }
    }

    if query:
        result.update({"Regular Expression": query})

    return result

# it start with anik and it accept 1 to 6 amount number
# there maybe one to six digit but must be one after anik
# localhost:9000/newitem/?query=anik7778

@app.get("/newitem")
async def read4(query: str=Query(default=None, min_length=3, max_length=15, regex="^anik\d{1,6}")):
    result = {
        "info" : {
            "name": "Anik Chandro",
            "id" : "18101070"
        }
    }

    if query:
        result.update({"Regular Expression": query})

    return result

# Query Default Values
# Default Value also make it optional

@app.get("/data")
async def read5(query: str=Query(default="slowlearn", min_length=5)):
    result = {
        "name":"Abu Bokker",
        "id": "18101082"
    }

    if query:
        result.update({"query": query})

    return result

# Required with Ellipsis (...)
# it is a special single value, it is part of Python and is called "Ellipsis", It is used by Pydantic and FastAPI to explicitly declare that a value is required.
@app.get("/required")
async def read6(query: str = Query(default=..., min_length=4, max_length=8)):
    result = {
        "name" : "Mahinur Alam",
        "id" : "18101023"
    }

    if query:
        result.update({"query":query})

    return result

# required by Required Keyword
@app.get("/newrequired")
async def read7(query: str=Query(default=Required, min_length=4, max_length=10)):
    result = {
        "name": "Md. Osim",
        "id" : "18101050"
    }

    result.update({"query": query})

    return result

# List query
# localhost:9000/list/?query=aubdur&query=rob&query=anik
@app.get("/list")
async def read8(query: List[str] = Query(default=Required, min_length=3, max_length=10)):
    result = {
        "query" : query
    }

    return result

@app.get("/newlist")
async def read8(query: List[str] = Query(default=["aubdur", "rob", "anik"], min_length=3, max_length=10)):
    result = {
        "query" : query
    }

    return result

@app.get("/newlst")
async def read8(query: list = Query(default=["aubdur", "rob", "anik"])):
    result = {
        "query" : query
    }

    return result

# Declare more metadata
# add title and description in query parameter

@app.get("/metadata")
async def read9(query: str=Query(default=None, title="Query String", description="Query String for the items to search in the database that have a good match", max_length=15)):
    result = {"item": "metadata"}

    if query:
        result.update({"query": query})

    return result

# Deprecating parameters

@app.get("/deprecated")
async def read10(query: str=Query(default=None, min_length=5, max_length=15, deprecated=True)):
    result = {"item": "Deprecated"}

    if query:
        result.update({"query": query})

    return result

# Alias parameters
# Imagine that you want the parameter to be item-query.
# Like in: http://127.0.0.1:8000/items/?item-query=foobaritems
# But item-query is not a valid Python variable name.
# The closest would be item_query.
# But you still need it to be exactly item-query...
# Then you can declare an alias

# localhost:9000/alias/?item-query=Aubdur Rob Anik
@app.get("/alias")
async def read11(item_query: str=Query(default=None, min_length=3, max_length=15, alias="item-query")):
    result = {"item": "Alias"}

    if item_query:
        result.update({"query":item_query})

    return result

# Exclue from OpenAPI

@app.get("/hidden")
async def read12(hidden_query: str=Query(default=None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not Found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('9000')))
