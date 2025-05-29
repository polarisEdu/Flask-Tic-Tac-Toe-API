from typing import Tuple, Optional, List
import random

from src.domain.service.game_service_interface import GameServiceInterface
from src.domain.model.game import Game
from src.domain.model.game_board import GameBoard


class GameService(GameServiceInterface):
    def get_next_move(self, game: Game) -> Tuple[int, int]:
        board = game.get_board().get_board()
        player = 2

        available_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    available_moves.append((i, j))

        if not available_moves:
            raise ValueError("No available moves")

        if len(available_moves) >= 8:
            return random.choice(available_moves)

        best_score = float('-inf')
        best_move = available_moves[0]

        for move in available_moves:
            i, j = move
            board[i][j] = player
            score = self._minimax(board, 0, False)
            board[i][j] = 0

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, board: List[List[int]], depth: int, is_maximizing: bool) -> float:
        temp_board = GameBoard(board)
        game_over, winner = self.check_game_over(temp_board)

        if game_over:
            if winner == 2:  # O won
                return 10 - depth
            elif winner == 1:  # X won
                return depth - 10
            else:  # Draw
                return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 2
                        score = self._minimax(board, depth + 1, False)
                        board[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            # X (human)
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        score = self._minimax(board, depth + 1, True)
                        board[i][j] = 0
                        best_score = min(score, best_score)
            return best_score

    def validate_game_board(self, game: Game, new_board: GameBoard) -> bool:
        current_board = game.get_board().get_board()
        updated_board = new_board.get_board()

        changes = 0
        for i in range(3):
            for j in range(3):

                if current_board[i][j] != 0 and current_board[i][j] != updated_board[i][j]:
                    return False
                if current_board[i][j] != updated_board[i][j]:
                    changes += 1

        if changes != 1:
            return False

        return True

    def check_game_over(self, board: GameBoard) -> Tuple[bool, Optional[int]]:
        board_state = board.get_board()
        for row in board_state:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return True, row[0]

        for col in range(3):
            if board_state[0][col] != 0 and board_state[0][col] == board_state[1][col] == board_state[2][col]:
                return True, board_state[0][col]

        if board_state[0][0] != 0 and board_state[0][0] == board_state[1][1] == board_state[2][2]:
            return True, board_state[0][0]

        if board_state[0][2] != 0 and board_state[0][2] == board_state[1][1] == board_state[2][0]:
            return True, board_state[0][2]

        if board.is_full():
            return True, 0

        return False, None

    def save_game(self, game: Game) -> None:
        raise NotImplementedError("must be implemented by child classes")

    def get_game(self, game_id: str) -> Optional[Game]:
        raise NotImplementedError("must be implemented by child classes")