from flask import Flask, send_from_directory
import os
from typing import Optional

from src.domain.service.game_service_interface import GameServiceInterface
from src.web.route.game_controller import game_routes, GameController


def create_app(game_service: GameServiceInterface) -> Flask:

    app = Flask(__name__, static_folder=None)

    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_SORT_KEYS'] = False

    GameController(game_service)

    app.register_blueprint(game_routes, url_prefix='/api')

    static_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')

    # маршрут для корневой страницы
    @app.route('/', methods=['GET'])
    def root():
        return send_from_directory(static_folder, 'index.html')

    # маршрут для статических файлов
    @app.route('/<path:path>', methods=['GET'])
    def static_files(path):
        return send_from_directory(static_folder, path)


    return app