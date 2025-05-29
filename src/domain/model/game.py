import uuid
from typing import Optional
from src.domain.model.game_board import GameBoard


class Game:
    def __init__(self, game_id: Optional[str] = None, board: Optional[GameBoard] = None):
        self.game_id = game_id if game_id else str(uuid.uuid4())
        self.board = board if board else GameBoard()

    def get_id(self) -> str:
        return self.game_id

    def get_board(self) -> GameBoard:
        return self.board

    def set_board(self, board: GameBoard) -> None:
        self.board = board