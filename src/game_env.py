from enum import Enum

import jericho.util
from jericho import *


class GameEnv:
    def __init__(self, game_path, seed = None, done = True):
        self.game_path      = game_path
        self.env            = None
        self.seed           = seed
        self.done           = done
        self.observation    = []
        self.info           = []
        self.reward         = []
        self.vocab          = None
        self.state          = None
        #self.initial_game()


    def run_loop(self):
        pass

    def initial_game(self):
        self.env = FrotzEnv(self.game_path)
        initial_observation, initial_info = self.env.reset()
        self.observation.append(initial_observation)
        self.info.append(initial_info)
        self.reward.append(0)
        print('*' * 10 + f"Running {self.game_path} game environment" + '*' * 10)
        print('=' * 50)
        print('*' * 10 + "Game Start!" + '*' * 10)
        print('-' * 50)
        print("obs:\n" + self.get_current_observation())
        print("info:\n" + self.get_current_info_in_str())

    def get_current_observation(self):
        return self.observation[-1]

    def get_observations(self):
        return self.observation

    def get_current_reward(self):
        return self.reward[-1]

    def get_rewards(self):
        return self.reward

    def get_current_info(self):
        return self.info[-1]

    def get_infos(self):
        return self.info

    def get_current_info_in_str(self):
        return str(self.info[-1])

    def get_infos_in_str(self):
        return str(self.info)

    def do_act(self, action):
        observation, reward, done, info = self.env.step(action)
        self.observation.append(observation)
        self.reward.append(reward)
        self.info.append(info)
        self.done = done

    # NEED TO DETERMINE THE NECESSARY
    def check_valid_actions(self):
        return jericho.util.recognized(self.get_current_observation())



class GameType(Enum):
    none = 0
    Zork_1 = 1


def get_game_by_name(game_name: str):
    match game_name:
        case "":
            return "", GameType.none
        case (GameType.Zork_1.name):
            return  "third-packages/z-machine-games-master/jericho-game-suite/zork1.z5", GameType.Zork_1

    return "", GameType.none

def get_game_by_index(game_index: int):
    match game_index:
        case (GameType.none.value):
            return "", GameType.none
        case (GameType.Zork_1.value):
            return  "third-packages/z-machine-games-master/jericho-game-suite/zork1.z5", GameType.Zork_1

    return "", GameType.none