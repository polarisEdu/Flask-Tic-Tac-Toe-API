from dataclasses import dataclass
from .game_board_dto import GameBoardDTO


@dataclass
class GameDTO:
    game_id: str
    board: GameBoardDTO

    def to_dict(self) -> dict:

        return {
            "game_id": self.game_id,
            "board": self.board.to_dict()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'GameDTO':

        return cls(
            game_id=data.get("game_id", ""),
            board=GameBoardDTO.from_dict(data.get("board", {"board": []}))
        )