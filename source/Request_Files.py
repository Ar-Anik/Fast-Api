import uvicorn
from fastapi import FastAPI, File, UploadFile
from pydantic import Required
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)

@app.post("/files/")
async def body1(file: bytes = File(default=None)):
    return {
        "file_size": len(file)
    }

@app.post("/uploadfile/")
async def body2(file: UploadFile = File(default=Required)):
    return {
        "filename": file.filename
    }


# Optional File Upload
@app.post("/optional/files/")
async def body3(file: bytes = File(default=None)):
    if not file:
        return {"message": "No File Sent"}
    else:
        return {"file_size": len(file)}

@app.post("/optional/uploadfile/")
async def body4(file: UploadFile = File(default=None)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


# UploadFile with Additional Metadata
@app.post("/meta/files/")
async def body5(file: bytes = File(default=Required, description="A file read as bytes")):
    return {
        "file_size": len(file)
    }

@app.post("/meta/uploadfile/")
async def body6(file: UploadFile = File(default=Required, description="A file read as UploadFile")):
    return {
        "filename": file.filename
    }


# Multiple File Uploads
@app.post("/multiple/files/")
async def body7(files: List[bytes] = File(default=Required)):
    return {
        "file_size": [len(i) for i in files]
    }

@app.post("/multiple/uploadfiles/")
async def body8(files: List[UploadFile] = File(default=Required)):
    return {
        "filenames": [i.filename for i in files]
    }

@app.get("/")
async def main():
    content = """
        <body>
            <form action="/multiple/files/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>

            <form action="/multiple/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
        </body>
    """
    return HTMLResponse(content=content)


# Multiple File Uploads with Additional Metadata
@app.post("/additional/files/")
async def body9(files: List[bytes] = File(default=None, description="Multiple Files as bytes")):
    return {
        "File Size": [len(i) for i in files]
    }

@app.post("/additional/uploadfiles/")
async def body10(files: List[UploadFile] = File(default=None, description="Multiple Files as UploadFile")):
    return {
        "filenames": [i.filename for i in files]
    }

@app.get("/")
async def main():
    content = """
        <body>
            <form action="/additional/files/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
            
            <form action="/additional/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
        </body>
    """

    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
