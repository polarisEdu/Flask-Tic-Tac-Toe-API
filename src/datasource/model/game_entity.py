from .game_board_entity import GameBoardEntity


class GameEntity:

    def __init__(self, game_id: str, board: GameBoardEntity):
        self.game_id = game_id
        self.board = board

    def get_id(self) -> str:
        return self.game_id

    def get_board(self) -> GameBoardEntity:
        return self.board