from src.Game.game_env import GameEnv


class ZorkEnv(GameEnv):
    def __init__(self, game_path):
        super().__init__(game_path)


