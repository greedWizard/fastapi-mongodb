from collections import defaultdict

from domain.users import UserModel
from repositories.users.common import ABCUserRepository
from services.exceptions import BadDataException


def validate_salary_gt(salary_gt: float) -> list[str]:
    errors = []

    if salary_gt is not None and salary_gt < 0:
        errors.append('Зарплата не может быть отрицательной')
    return errors


def validate_salary_lt(salary_lt: float) -> list[str]:
    errors = []

    if salary_lt is not None and salary_lt < 0:
        errors.append('Зарплата не может быть отрицательной')
    return errors


def validate_name(name: str) -> list[str]:
    errors = []

    if name is not None and not name:
        errors.append('Имя не может быть пустым')
    return errors


def validate_limit(limit: int) -> list[str]:
    errors = []

    if limit is not None and limit <= 0:
        errors.append('Количество объектов на странице не может быть меньше чем 0')
    return errors


def validate_skip(skip: int) -> list[str]:
    errors = []

    if skip is not None and skip < 0:
        errors.append('Нельзя пропустить меньше чем 0 элементов')
    return errors


def validate_ordering(ordering: str) -> list[str]:
    errors = []

    if ordering is None:
        return errors

    check_ordering = ordering[1:] if ordering.startswith('-') else ordering

    if check_ordering not in UserModel.__fields__:
        errors.append('Нельзя сортировать по данному полю')
    return errors


def validate_fetch_fields(
    salary_gt: float | None = None,
    salary_lt: float | None = None,
    name: str | None = None,
    limit: int = 10,
    skip: int = 0,
    ordering: str = 'name',
) -> dict:
    errors = defaultdict(list)

    errors['salary_gt'] = validate_salary_gt(salary_gt)
    errors['salary_lt'] = validate_salary_lt(salary_lt)
    errors['name'] = validate_name(name)
    errors['limit'] = validate_limit(limit)
    errors['skip'] = validate_skip(skip)
    errors['ordering'] = validate_ordering(ordering)

    return {
        field: field_errors for field, field_errors in errors.items()
        if len(field_errors) > 0
    }


async def fetch_users(
    repository: ABCUserRepository,
    salary_gt: float | None = None,
    salary_lt: float | None = None,
    name: str | None = None,
    limit: int = 10,
    skip: int = 0,
    ordering: str = 'name',
) -> list[UserModel]:
    errors = validate_fetch_fields(
        salary_gt,
        salary_lt,
        name,
        limit,
        skip,
        ordering,
    )

    if errors:
        raise BadDataException(errors)

    users = await repository.fetch(
        salary_gt,
        salary_lt,
        name,
        limit,
        skip,
        ordering,
    )
    users_count = await repository.count(
        salary_gt,
        salary_lt,
        name,
    )
    return users, users_count
