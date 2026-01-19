from dataclasses import fields
from tortoise.models import Model
from pydantic import BaseModel
from tortoise import models, fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    myfield = fields.CharField(max_length=255, null=True)
    

class Expense(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    amount = fields.FloatField()
    category = fields.CharField(max_length=50)
    user = fields.ForeignKeyField("models.User", related_name="expenses", on_delete=fields.CASCADE
    )

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    

    class Config:
        orm_mode = True
