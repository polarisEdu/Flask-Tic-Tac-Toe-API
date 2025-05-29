from src.domain.model.game import Game
from src.domain.model.game_board import GameBoard
from src.datasource.model.game_entity import GameEntity
from src.datasource.model.game_board_entity import GameBoardEntity


class GameMapper:
    @staticmethod
    def to_entity(game: Game) -> GameEntity:

        board_entity = GameBoardEntity(game.get_board().get_board())

        return GameEntity(game.get_id(), board_entity)

    @staticmethod
    def to_domain(game_entity: GameEntity) -> Game:
        board = GameBoard(game_entity.get_board().get_board())
        return Game(game_entity.get_id(), board)