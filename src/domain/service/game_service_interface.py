"""
Game service interface definition.
"""

from abc import ABC, abstractmethod
from typing import Tuple, Optional

from src.domain.model.game import Game
from src.domain.model.game_board import GameBoard


class GameServiceInterface(ABC):
    @abstractmethod
    def get_next_move(self, game: Game) -> Tuple[int, int]:
        pass

    @abstractmethod
    def validate_game_board(self, game: Game, new_board: GameBoard) -> bool:
        pass

    @abstractmethod
    def check_game_over(self, board: GameBoard) -> Tuple[bool, Optional[int]]:
        pass

    @abstractmethod
    def save_game(self, game: Game) -> None:
        pass

    @abstractmethod
    def get_game(self, game_id: str) -> Optional[Game]:
        pass