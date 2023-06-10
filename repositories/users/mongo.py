from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime

from pymongo import MongoClient, ASCENDING, DESCENDING
from domain.users import GenderEnum, UserModel

from repositories.users.common import ABCUserRepository


@dataclass(frozen=True)
class UsersMongoRepository(ABCUserRepository):
    client: MongoClient  # TODO: можно воткнуть асинхронный клиент монги MOTOR, но мне лень
                            # так как уже привык работать с этим
    db_name: str
    collection_name: str

    async def count(
        self,
        salary_gt: float | None = None,
        salary_lt: float | None = None,
        name: str | None = None,
    ) -> list[UserModel]:
        collection = self.client[self.db_name][self.collection_name]
        find_query = self.get_find_query(salary_gt, salary_lt, name)

        return collection.count_documents(find_query)

    def get_find_query(self, salary_gt, salary_lt, name):
        find_query = defaultdict(dict)

        if salary_gt is not None:
            find_query['salary']['$gt'] = salary_gt
        if salary_lt is not None:
            find_query['salary']['$lt'] = salary_lt
        if name is not None:
            find_query['name']['$regex'] = f'{name}'  # TODO: сделать невосприимчивость к регистру
        return find_query

    async def fetch(
        self,
        salary_gt: float | None = None,
        salary_lt: float | None = None,
        name: str | None = None,
        limit: int = 10,
        skip: int = 0,
        ordering: str = 'name',
    ) -> list[UserModel]:
        collection = self.client[self.db_name][self.collection_name]

        find_query = self.get_find_query(salary_gt, salary_lt, name)

        sort_by_field = ordering[1:] if ordering.startswith('-') else ordering
        order = DESCENDING if ordering.startswith('-') else ASCENDING

        return [
            document for document in
            collection.find(find_query, limit=limit, skip=skip).sort(sort_by_field, order)
        ]

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
        collection = self.client[self.db_name][self.collection_name]
        inserted_document = {
            'name': name,
            'email': email,
            'age': age,
            'company': company,
            'join_date': join_date,
            'job_title': job_title,
            'gender': gender,
            'salary': salary,
        }
        result = collection.insert_one(inserted_document)

        return UserModel(_id=result.inserted_id, **inserted_document)
