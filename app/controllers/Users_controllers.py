
from argon2 import hash_password, verify_password
from app.helpers.auth_helpers import create_token, hash_password
from fastapi import APIRouter, FastAPI, HTTPException
from app.models.user import User
from app.schemas import LoginUser, Usercreate
from app.helpers.auth_helpers import verify_password


app = FastAPI()

router = APIRouter(
    tags=["users"],
)
@router.post("/signup/")
async def signup(user: Usercreate):

    exists = await User.filter(email=user.email).exists()
    if exists:
        raise HTTPException(status_code=400, detail="User already exists")

    user = await User.create(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        # myfield="default_value",
        # role="expenses"
    )

    return {"message": "User created successfully", "expenses_id": user.id}


@router.post("/login/")  
async def login(user: LoginUser):
     existing_user = await User.get_or_none(email=user.email)
     if not existing_user:
        raise HTTPException(404, "User not found")
     if not verify_password(user.password, existing_user.password):
        raise HTTPException(401, "Invalid password")
     
     token = create_token({"user_id": existing_user.id})
     return {"access_token": token, "token_type": "bearer"}
