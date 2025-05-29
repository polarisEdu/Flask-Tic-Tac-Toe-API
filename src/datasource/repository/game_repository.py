from typing import Optional

from src.domain.model.game import Game
from src.datasource.repository.game_repository_interface import GameRepositoryInterface
from src.datasource.repository.game_storage import GameStorage
from src.datasource.mapper.game_mapper import GameMapper


class GameRepository(GameRepositoryInterface):

    def __init__(self, storage: GameStorage):
        self._storage = storage

    def save(self, game: Game) -> None:
        game_entity = GameMapper.to_entity(game)
        self._storage.save(game_entity)

    def get(self, game_id: str) -> Optional[Game]:
        game_entity = self._storage.get(game_id)

        if game_entity is None:
            return None

        return GameMapper.to_domain(game_entity)