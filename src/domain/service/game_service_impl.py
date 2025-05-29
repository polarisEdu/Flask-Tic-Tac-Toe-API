from typing import Optional

from src.domain.model.game import Game
from src.domain.service.game_service import GameService
from src.datasource.repository.game_repository_interface import GameRepositoryInterface


class GameServiceImpl(GameService):
    def __init__(self, repository: GameRepositoryInterface):
        self._repository = repository

    def save_game(self, game: Game) -> None:
        self._repository.save(game)

    def get_game(self, game_id: str) -> Optional[Game]:
        return self._repository.get(game_id)

    def make_move(self, game_id: str, row: int, col: int) -> Optional[Game]:
        game = self.get_game(game_id)

        if game is None:
            return None

        board = game.get_board()

        #  make move  X - 1
        if not board.set_cell(row, col, 1):
            return None

        game_over, _ = self.check_game_over(board)

        if not game_over:
            computer_row, computer_col = self.get_next_move(game)
            board.set_cell(computer_row, computer_col, 2)

        self.save_game(game)

        return game