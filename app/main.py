from fastapi import FastAPI
from app.controllers import Users_controllers, expenses_controllers
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
import os 

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres.oolarqdovqxdpqzxlbjx:javeria1529@aws-1-ap-northeast-2.pooler.supabase.com:6543/postgres?statement_cache_size=0"
    },
    
    "apps": {
        "models": {
            "models": [
                "app.models.user", "aerich.models",    
            ],
            "default_connection": "default",
        }
    }
}


async def init():
    await Tortoise.init(config = TORTOISE_ORM)
    await Tortoise.generate_schemas()
        


async def lifespan(app: FastAPI):
    await init()
    print("Connected to database")
    yield
    print("Shutdown")
    await Tortoise.close_connections()

app = FastAPI(titel='tracker API', lifespan=lifespan)

app.include_router(Users_controllers.router)
app.include_router(expenses_controllers.router)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3", 
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


# javeria1529 password