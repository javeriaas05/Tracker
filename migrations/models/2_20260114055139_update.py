from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "expense" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "category" VARCHAR(50) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
        ALTER TABLE "user" DROP COLUMN "role";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "role" VARCHAR(50) NOT NULL DEFAULT 'user';
        DROP TABLE IF EXISTS "expense";"""


MODELS_STATE = (
    "eJztmF9v2jAQwL8K4qmTuqllZa32FijVWDuo6JgmVVVkkiNYdezUdtaiiu8+20lwCAmDCS"
    "SQeEvuT3z34+w7/F4PmQ9EfOq8RUAF1L/W3usUhfqhqDqt1VEUWYUWSDQixhZyRiMhOfKk"
    "Eo8REaBEPgiP40hiRpWUxoRoIfOUIaaBFcUUv8TgShaAnABXiscnJcbUhzcQ2Wv07I4xEH"
    "8hWOzrtY3cldPIyLpU3hhDvdrI9RiJQ2qNo6mcMDq3xlRqaQAUOJKgPy95rMPX0aWJZhkl"
    "kVqTJMScjw9jFBOZS3dNBh6jmp+KRpgEA73Kx8b5xeXF1ecvF1fKxEQyl1zOkvRs7omjId"
    "D7WZ8ZPZIosTAYLTeJJYFldO0J4uXs5g4FfCroIr4M1ip+mcACtEWzJYIhenMJ0EBO1Ov5"
    "2dkKXr+cQfubMzhRVh90NkwVclLgvVTVSHQaqoWIQhYn1bNI8YYwVFGC1qXAcax99pPkCn"
    "DX/WHrrlO7H3Ta3Yduv6cTCKfihVilFikBlibNQce5K1D0VLIB49NNqjHvc5gF2VynHpvV"
    "5dhcqsZYAHc3Og9zHv8+FPcE4hbORd1Mxs+lx6ImUrKfGQcc0FuYGo5dFRGiXtlpmPbOYf"
    "qZ/eM3y2ogk9rWxdHrvMHmS0Olp5KCZP+2nYe2c92pG4gj5D2/Iu67CzS1hjVYQTK3XVaF"
    "jbAoQRQFJn+dhY45D7ZkWMmAV08q2S97HFP2bTuuGlP0r2aeN+gNeZ/t9IadU9xxZ4AQYb"
    "IJwrnDIfJrNJtrAFRWlQSNbhFhhIR4ZbxkG1dTzPsc5pCyE5ThdJzhWpdkzuW/QKb1dvgc"
    "l0aX6jac2/7Jn3SxTLyVet7cDoAgk2PlTJO7D9i/sq0aa2a7HEYc4NiblI0jqWblQIKszX"
    "EkOaCR5A9wkW6UdY+vnMuxD9jbE7U1NoCYmh8mwJ1cP6kVJZTdP31/6Pcq7k2sSwHkkKoE"
    "H33sydMawUI+7SfWFRR11ub+SaT3Txm8kx/O7yLX9l2/ZSgwIQNuvmI+0NqsyW6/vcz+At"
    "eNjfk="
)
