from typing import List


class GameBoardEntity:

    def __init__(self, board: List[List[int]]):
        self.board = board

    def get_board(self) -> List[List[int]]:
        return self.board