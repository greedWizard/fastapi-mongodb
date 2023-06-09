from fastapi import Query
from fastapi.routing import APIRouter

from domain.users import UserModel


router = APIRouter(tags=['users'], prefix='/users')


@router.get(
    '/',
    response_model=list[UserModel],
    description='Получить список пользователей',
    summary='Взять список доступных пользователей из БД',
    operation_id='getUsers',
)
def get_users_handler(
    salary__gte: int = Query(
        default=None,
        description='Заработная плата работников больше чем',
    ),
    salary__lte: int = Query(
        default=None,
        description='Заработная плата работников меньше чем',
    ),
    name: str = Query(
        default=None,
        description='Поиск по имени пользователя',
    )
):
    return []
