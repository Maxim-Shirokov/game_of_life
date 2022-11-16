from enum import Enum

from pydantic import BaseModel


class ErrorObj(BaseModel):
    type: str
    message: str


class BasicErrorTypes(str, Enum):
    UNKNOWN_TYPE = 'unknown_type'
    FORBIDDEN = 'forbidden'
    NOT_FOUND = 'not_found'
    UNPROCESSABLE_ENTITY = 'unprocessable_entity'
    INTERNAL_SERVER = 'internal_server'
    SERVICE_UNAVAILABLE = 'service_unavailable'


class BasicError:
    @staticmethod
    def get_unknown_type_error() -> ErrorObj:
        return ErrorObj(type=BasicErrorTypes.UNKNOWN_TYPE, message='Unknown type')

    @staticmethod
    def get_forbidden_error() -> ErrorObj:
        return ErrorObj(type=BasicErrorTypes.FORBIDDEN, message='Forbidden')

    @staticmethod
    def get_not_found_error(obj: str = '') -> ErrorObj:
        return ErrorObj(type=BasicErrorTypes.NOT_FOUND, message=f'Not found {obj if obj else "object"}')

    @staticmethod
    def get_unprocessable_entity_error(extra: str = '') -> ErrorObj:
        return ErrorObj(
            type=BasicErrorTypes.UNPROCESSABLE_ENTITY, message=f'Unprocessable entity{f" {extra}" if extra else ""}'
        )

    @staticmethod
    def get_internal_server_error() -> ErrorObj:
        return ErrorObj(type=BasicErrorTypes.INTERNAL_SERVER, message='Something went wrong, please try again')

    @staticmethod
    def get_service_unavailable_error() -> ErrorObj:
        return ErrorObj(
            type=BasicErrorTypes.SERVICE_UNAVAILABLE, message='The server is currently unable to handle the request'
        )
