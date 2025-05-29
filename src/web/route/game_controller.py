from flask import Blueprint, request, jsonify, Response
import json
import uuid
from typing import Tuple, Dict, Any, Optional

from src.domain.service.game_service_interface import GameServiceInterface
from src.domain.model.game_board import GameBoard
from src.domain.model.game import Game
from src.web.mapper.game_mapper import GameWebMapper
from src.web.model.game_dto import GameDTO
from src.web.model.game_board_dto import GameBoardDTO


game_routes = Blueprint('game_routes', __name__)


class GameController:
    def __init__(self, game_service: GameServiceInterface):

        self._game_service = game_service
        self._register_routes()

    def _register_routes(self) -> None:

        game_routes.route('/game', methods=['POST'])(self.create_game)
        game_routes.route('/game/<game_id>', methods=['GET'])(self.get_game)
        game_routes.route('/game/<game_id>', methods=['POST'])(self.update_game)

    def create_game(self) -> Tuple[Response, int]:
        game = Game()
        self._game_service.save_game(game)

        game_dto = GameWebMapper.to_dto(game)

        return jsonify(game_dto.to_dict()), 201

    def get_game(self, game_id: str) -> Tuple[Response, int]:
        game = self._game_service.get_game(game_id)

        if game is None:
            return jsonify({"error": "Game not found"}), 404

        game_dto = GameWebMapper.to_dto(game)

        return jsonify(game_dto.to_dict()), 200

    def update_game(self, game_id: str) -> Tuple[Response, int]:

        try:
            data = request.json
            if not data:
                return jsonify({"error": "Invalid request data"}), 400

            game_dto = GameDTO(
                game_id=game_id,
                board=GameBoardDTO.from_dict(data.get("board", {}))
            )
            updated_game = GameWebMapper.to_domain(game_dto)

            current_game = self._game_service.get_game(game_id)
            if current_game is None:
                return jsonify({"error": "Game not found"}), 404

            if not self._game_service.validate_game_board(current_game, updated_game.get_board()):
                return jsonify({"error": "Invalid game board update"}), 400

            game_over, winner = self._game_service.check_game_over(updated_game.get_board())

            if game_over:
                current_game.set_board(updated_game.get_board())
                self._game_service.save_game(current_game)

                response = {
                    **GameWebMapper.to_dto(current_game).to_dict(),
                    "game_over": True,
                    "winner": self._get_winner_message(winner)
                }

                return jsonify(response), 200

            # Делаем ход компьютера
            # Обновляем текущую игру
            current_game.set_board(updated_game.get_board())

            # Получаем координаты хода компьютера
            computer_row, computer_col = self._game_service.get_next_move(current_game)

            # Делаем ход компьютера (компьютер ходит ноликами - 2)
            current_game.get_board().set_cell(computer_row, computer_col, 2)

            self._game_service.save_game(current_game)

            # Проверяем, окончена ли игра после хода компьютера
            game_over, winner = self._game_service.check_game_over(current_game.get_board())

            # ответ
            response = {
                **GameWebMapper.to_dto(current_game).to_dict(),
                "game_over": game_over
            }

            if game_over:
                response["winner"] = self._get_winner_message(winner)

            return jsonify(response), 200

        except Exception as e:
            import traceback
            traceback.print_exc()
            return jsonify({"error": f"Error processing move: {str(e)}"}), 500


    def _get_winner_message(self, winner: Optional[int]) -> str:
        if winner == 1:
            return "X wins"
        elif winner == 2:
            return "O wins"
        else:
            return "Draw"