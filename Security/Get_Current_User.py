from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import uvicorn

app = FastAPI(debug=True)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disable: str = None

def fake_decode_token(token):
    return User(username=token + "fakedecoded", email="anik@gmail.com", full_name="John Doe", disable="false")

async def get_current_user(token: str = Depends(oauth2_schema)):
    print(token)
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

