from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .errors import ErrorObj


class SuccessResponse(BaseModel):
    success: bool = True


class ErrorResponse(BaseModel):
    type: str
    message: str


def success_response():
    return JSONResponse(status_code=200, content=SuccessResponse().dict())


def error_response(err: ErrorObj, status_code: int = 400):
    return JSONResponse(status_code=status_code, content=err.dict())
