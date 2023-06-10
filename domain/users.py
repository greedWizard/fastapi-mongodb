from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class GenderEnum(str, Enum):
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'


class UserModel(BaseModel):
    _id: str
    name: str
    email: str
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: GenderEnum
    salary: float

    class Config:
        orm_mode = True
