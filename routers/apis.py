from fastapi import APIRouter
from routers.api_v1 import games, players, clubs, leagues,game_pve

api_router = APIRouter()
# router注册
api_router.include_router(games.router, prefix='/games', tags=['game api'])
api_router.include_router(players.router, prefix='/players', tags=['player api'])
api_router.include_router(clubs.router, prefix='/clubs', tags=['club api'])
api_router.include_router(leagues.router, prefix='/leagues', tags=['league api'])
api_router.include_router(game_pve.router, prefix='/game-pve', tags=['game pve api'])

