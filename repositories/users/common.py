from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.users import GenderEnum, UserModel


@dataclass(frozen=True)
class ABCUserRepository(ABC):
    async def fetch(
        self,
        salary_gt: float | None = None,
        salary_lt: float | None = None,
        name: str | None = None,
        limit: int = 10,
        skip: int = 0,
        ordering: str = 'name',
    ) -> list[UserModel]:
        ...

    async def insert(
        self,
        name: str,
        email: str,
        age: int,
        company: str,
        join_date: datetime,
        job_title: str,
        gender: GenderEnum,
        salary: float,
    ) -> UserModel:
        ...

