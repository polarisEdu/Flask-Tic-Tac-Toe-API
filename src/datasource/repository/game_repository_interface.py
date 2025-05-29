from abc import ABC, abstractmethod
from typing import Optional

from src.domain.model.game import Game


class GameRepositoryInterface(ABC):

    @abstractmethod
    def save(self, game: Game) -> None:
        pass

    @abstractmethod
    def get(self, game_id: str) -> Optional[Game]:
        pass