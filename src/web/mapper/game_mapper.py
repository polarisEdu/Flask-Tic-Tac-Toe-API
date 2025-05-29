from src.domain.model.game import Game
from src.domain.model.game_board import GameBoard
from src.web.model.game_dto import GameDTO
from src.web.model.game_board_dto import GameBoardDTO


class GameWebMapper:

    @staticmethod
    def to_dto(game: Game) -> GameDTO:

        # в DTO для web
        board_dto = GameBoardDTO(board=game.get_board().get_board())
        return GameDTO(game_id=game.get_id(), board=board_dto)

    @staticmethod
    def to_domain(game_dto: GameDTO) -> Game:
        # в доменную модель
        board = GameBoard(game_dto.board.board)

        return Game(game_id=game_dto.game_id, board=board)