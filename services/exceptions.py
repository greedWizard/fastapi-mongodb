from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceException(Exception):
    errors: dict[str, list]


@dataclass(frozen=True)
class BadDataException(ServiceException):
    ...
