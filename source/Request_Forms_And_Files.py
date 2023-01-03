import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import Required

app = FastAPI(debug=True)

@app.post("/files/")
async def create_file(file: bytes = File(default=Required), fileb: UploadFile = File(default=Required), token: str = Form(default=Required)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
