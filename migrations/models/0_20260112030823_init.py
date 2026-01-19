from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "myfield" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm9r2zAQxr9K8KsOupF6yVr2Lg2MbWwpdOsYlGIUW7FFZMmVzmtDyXevTrYj2flDAo"
    "MudO/s556T7n6xdHkKcplQrt/daKqCj72nQJCcmoeWftoLSFE4FQUgU26NZeOYalAkBqPN"
    "CNfUSAnVsWIFMCmMKkrOUZSxMTKROqkU7L6kEciUQmbruL0zMhMJfaS6eS3m0YxRnrTKZA"
    "nubfUIFoXVvgj4ZI242zSKJS9z4czFAjIpVm4mANWUCqoIUFweVInlY3V1l01HVaXOUpXo"
    "5SR0RkoOXrt7MoilQH6mGm0bTHGXt+HZ4Hxw8f7D4MJYbCUr5XxZted6rxItgcnPYGnjBE"
    "jlsBgdN/zV7PMavXFG1GZ8fk4Hoim9C7FB9qIUc/IYcSpSyMzrsL8D2a/R9fjz6Ppk2H+D"
    "nUjzKVff96SOhDaEVB1FmhPGD0G4SjhGfuFwuAdA49pK0MbaCAui9YNUG47xdop+zt8B2Q"
    "iOpLvDjgZlvpg1uPYl6aW8cpA4YWZz765EYUri+QNRSbQWkaHc5l0P5WHeVYggqcWDTWIH"
    "9bwdUcXibNMkriM7ZzFxnv/T+Iim8R+qNJZ0wMn1Ul75yfWvQDwaB0Cs7ccJ8Ky/z/8Z49"
    "oK0MbaAM2OQKsz2Ib49cfVZDNEL6UD8kaYBm8TFsNpjzMNd/8m1h0UsWssOtf6nvvwTr6P"
    "fne5jr9dXVoKUkOq7Cp2gcuXHi/LZyHnbOg="
)
