from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def update_admit():
    return {
        "message": "Admin Getting schwifty"
    }
