
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr

class Usercreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseUpdate(BaseModel):
    title: str
    amount: float
    category: str

