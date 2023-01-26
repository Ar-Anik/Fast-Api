from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
import uvicorn

database = {
    "anik": {
        "username": "aranik",
        "full_name": "Aubdur Rob Anik",
        "email": "aranik@gmail.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "sukon": {
        "username": "ssukon",
        "full_name": "salman sukon",
        "email": "ssukon@gmail.com",
        "hashed_password": "fakehashedsecret",
        "disabled": True,
    },
}

app = FastAPI(debug=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None

class UserInDB(User):
    hashed_password: str


def hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def decode_token(token):
    user = get_user(database, token)

    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authentication Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive User")

    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.__dict__)
    user_dict = database.get(form_data.username)

    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Username")

    user = UserInDB(**user_dict)
    Hash_Password = hash_password(form_data.password)
    if not Hash_Password == user.hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrent Password")

    return {
        "access_token": user.username,
        "token_type": "bearer",
    }

@app.get("/users/me")
async def user_information(current_user: User = Depends(get_current_active_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))
