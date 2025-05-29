from typing import Dict, Any

from src.datasource.repository.game_storage import GameStorage
from src.datasource.repository.game_repository import GameRepository
from src.domain.service.game_service_impl import GameServiceImpl
from src.domain.service.game_service_interface import GameServiceInterface
from src.web.module.app import create_app
from flask import Flask


class Container:

    def __init__(self):

        self._instances: Dict[str, Any] = {}

    def get_game_storage(self) -> GameStorage:

        if 'game_storage' in self._instances:
            return self._instances['game_storage']

        storage = GameStorage()
        self._instances['game_storage'] = storage

        return storage

    def get_game_repository(self) -> GameRepository:
        return GameRepository(self.get_game_storage())

    def get_game_service(self) -> GameServiceInterface:
        return GameServiceImpl(self.get_game_repository())

    def get_flask_app(self) -> Flask:
        return create_app(self.get_game_service())