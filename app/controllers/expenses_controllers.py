from fastapi import APIRouter, Depends, FastAPI, HTTPException
from app.models.user import ExpenseCreate, User
from app.models.user import Expense
from app.schemas import ExpenseCreate, ExpenseUpdate
from app.Dependencies import get_current_user


app = FastAPI()

router = APIRouter(
    tags = ["expenses"]
)


@router.get("/expenses")
async def expenses(current_user: User = Depends(get_current_user)):
    return await Expense.filter(user_id=current_user.id).all()

@router.post("/expenses")
async def creat_expenses(expense: ExpenseCreate,
    current_user: User = Depends(get_current_user)
):
    new_expenses = await Expense.create(
        title=expense.title,
        amount=expense.amount,        
        category=expense.category,
        user_id=current_user.id
    )
    return new_expenses

@router.get("/expense/{expense_id}")
async def get_expense(
    expense_id: int,
    current_user: User = Depends(get_current_user)
):
    expense = await Expense.get_or_none(
        id=expense_id,
        user_id=current_user.id
    )
    if not expense:
        raise HTTPException(404, "Expense not found")

    return expense


@router.put("/expense/{expense_id}")
async def update_expense(expense_id: int, expense: ExpenseUpdate, current_user: User = Depends(get_current_user)
):
    db_expense = await Expense.get_or_none(
        id=expense_id,
        user_id=current_user.id
    )
    if not db_expense:
        raise HTTPException(403, "Not allowed")

    db_expense.title = expense.title
    db_expense.amount = expense.amount
    db_expense.category = expense.category
    await db_expense.save()
    return db_expense

@router.delete("/expense/{expense_id}")
async def delete_expense(
    expense_id: int,
    current_user: User = Depends(get_current_user)
):
    expense = await Expense.get_or_none(
        id=expense_id,
        user_id=current_user.id
    )
    if not expense:
        raise HTTPException(403, "Not allowed")

    await expense.delete()
    return {"message": "Expense deleted"}
