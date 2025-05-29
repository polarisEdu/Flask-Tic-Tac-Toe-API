from typing import List
from dataclasses import dataclass


@dataclass
class GameBoardDTO:
    board: List[List[int]]

    def to_dict(self) -> dict:
        """
         в JSON.
        """
        return {
            "board": self.board
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'GameBoardDTO':
        """ из JSON).   """
        return cls(board=data.get("board", []))