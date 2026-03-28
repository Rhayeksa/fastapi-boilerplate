# from src.api.v1.battle.route import router as battle_v1
# from src.api.v1.user.route import router as user_v1
from src.api.welcome_api import router as welcome_api

routes = [
    welcome_api,
    # user_v1,
    # battle_v1,
]
