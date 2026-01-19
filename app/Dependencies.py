
from fastapi import Depends, HTTPException
from app.helpers.auth_helpers import verify_token
from app.models.user import User

async def get_current_user(current_user: User = Depends(verify_token))-> User:
    return current_user

async def get_current_user_id(current_user: User = Depends(verify_token)) -> int:
    return current_user.id


