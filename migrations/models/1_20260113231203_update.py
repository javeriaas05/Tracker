from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "role" VARCHAR(50) NOT NULL DEFAULT 'user';
        ALTER TABLE "user" ALTER COLUMN "myfield" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "role";
        ALTER TABLE "user" ALTER COLUMN "myfield" SET NOT NULL;"""


MODELS_STATE = (
    "eJztlmtr2zAUhv9KyKcWupF6yVr2LQ2MbWwpdOsYlGIU+9gWkSVXkteGkv8+Hfki27mQlL"
    "E2o9/s97zHOuexbo/9VITA1NtrBbL/offY5yQF89DST3p9kmVORUGTGbPGvHLMlJYk0EaL"
    "CFNgpBBUIGmmqeBG5TljKIrAGCmPnZRzepeDr0UMOrF13NwamfIQHkBVr9ncjyiwsFUmDX"
    "Fsq/t6kVntM9cfrRFHm/mBYHnKnTlb6ETw2k25RjUGDpJowM9rmWP5WF3ZZdVRUamzFCU2"
    "ckKISM50o90dGQSCIz9TjbINxjjKG+90eDY8f/d+eG4stpJaOVsW7bnei0RLYPqjv7Rxok"
    "nhsBgdN/xr9nmF3iQhcj2+Zk4Hoim9C7FC9qwUU/LgM+CxTszraLAF2c/x1eTT+OpoNDjG"
    "ToSZysX8npYRz4aQqqMIKaFsH4R1wiHy80ajHQAa10aCNtZGmBGl7oVcs4w3U2zm/B2Qle"
    "BIuj3sYFCmi6jCtSvJRsqTQJbz7f/iKAXba1+s/P9uKtaH7gvaF/GIjuaNwwaFGQnm90SG"
    "/kpEeGKTdzWUemlXIZzElg52iPWXF5YxSBok664yZWTrZYY4z+t15oCuM79BKixpj1XbSH"
    "k9Q2qQuDT2gFjaDxPg6WCXjc+4NgK0sTZAM6KGYg22IX75fjldD7GR0gF5zU2DNyEN9EmP"
    "UaVvXybWLRSxayw6VeqONeEdfRv/6nKdfL28sBSE0rG0X7EfuHju42X5B3q60mI="
)
