from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse

from app.pkg.responses import ErrorResponse, SuccessResponse, error_response, success_response

from .dependencies import get_game_service
from .dto.requests import GameIn
from .dto.responses import GameOut
from .services import GameService

game_router = APIRouter(prefix='/game', tags=['game'], responses={404: {'description': 'Not Found'}})


@game_router.post('', responses={200: {'model': SuccessResponse}, 400: {'model': ErrorResponse}})
def new_game(data: GameIn = Body(...), game_service: GameService = Depends(get_game_service)) -> JSONResponse:
    game_service.create_game(height=data.height, width=data.width)
    return success_response()


@game_router.post('/next', responses={200: {'model': GameOut}, 400: {'model': ErrorResponse}})
def next_step(game_service: GameService = Depends(get_game_service)) -> JSONResponse:
    res, err = game_service.next_step()
    if err:
        return error_response(err)
    return JSONResponse(status_code=200, content=res.dict())
