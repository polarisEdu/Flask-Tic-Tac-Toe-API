from typing import List, Optional


class GameBoard:
    def __init__(self, board: Optional[List[List[int]]] = None):
        if board is None:
            self.board = [[0 for _ in range(3)] for _ in range(3)]
        else:
            self.board = board

    def get_board(self) -> List[List[int]]:
        return self.board

    def set_cell(self, row: int, col: int, value: int) -> bool:
        if not (0 <= row < 3 and 0 <= col < 3):
            return False

        if not (0 <= value <= 2):
            return False

        if self.board[row][col] != 0 and value != 0:
            return False

        self.board[row][col] = value
        return True

    def is_full(self) -> bool:
        for row in self.board:
            if 0 in row:
                return False
        return True

    def is_empty(self) -> bool:
        for row in self.board:
            if any(cell != 0 for cell in row):
                return False
        return True

    def __eq__(self, other):
        if not isinstance(other, GameBoard):
            return False

        return self.board == other.board