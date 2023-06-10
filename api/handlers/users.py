from dependency_injector.wiring import inject, Provide

from fastapi import Depends, HTTPException, Query
from fastapi.routing import APIRouter

from starlette import status
from api.schemas.users import UserResponseSchema

from repositories.users.mongo import UsersMongoRepository
from common.containers.users import UserContainer
from services.exceptions import BadDataException
from services.users import fetch_users


router = APIRouter(tags=['users'], prefix='/users')


@router.get(
    '/',
    response_model=UserResponseSchema,
    description='Получить список пользователей',
    summary='Взять список доступных пользователей из БД',
    operation_id='getUsers',
)
@inject
async def get_users_handler(
    salary_gt: int = Query(
        default=None,
        description='Заработная плата работников больше чем',
    ),
    salary_lt: int = Query(
        default=None,
        description='Заработная плата работников меньше чем',
    ),
    name: str = Query(
        default=None,
        description='Поиск по имени пользователя',
    ),
    limit: int = Query(
        default=10,
        description='Количество объектов в ответе',
    ),
    offset: int = Query(
        default=0,
        description='С какого объекта начинать выборку',
    ),
    ordering: str = Query(
        default='name',
        description='Порядок сортировки',
    ),
    repository: UsersMongoRepository = Depends(
        Provide[UserContainer.user_repository],
    )
):
    try:
        users, count = await fetch_users(
            repository,
            salary_gt,
            salary_lt,
            name,
            limit,
            offset,
            ordering,
        )
    except BadDataException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.errors,
        )

    return UserResponseSchema(
        count=count,
        users=users,
    )
