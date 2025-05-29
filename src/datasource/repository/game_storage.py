from multiprocessing import Manager
from typing import Optional
from src.datasource.model.game_entity import GameEntity


class GameStorage:
    def __init__(self):
        manager = Manager()
        self._games = manager.dict()

    def save(self, game: GameEntity) -> None:
        self._games[game.get_id()] = game

    def get(self, game_id: str) -> Optional[GameEntity]:
        return self._games.get(game_id)






# from typing import Dict, Optional

# import threading
#
# from src.datasource.model.game_entity import GameEntity
#
#
# class GameStorage:
#
#     def __init__(self):
#         self._games: Dict[str, GameEntity] = {}
#
#         self._lock = threading.RLock()
#
#     def save(self, game: GameEntity) -> None:
#         with self._lock:
#             self._games[game.get_id()] = game
#
#     def get(self, game_id: str) -> Optional[GameEntity]:
#         with self._lock:
#             return self._games.get(game_id)