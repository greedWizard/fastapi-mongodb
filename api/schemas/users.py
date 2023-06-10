from pydantic import BaseModel

from domain.users import UserModel


class UserResponseSchema(BaseModel):
    count: int
    users: list[UserModel]
