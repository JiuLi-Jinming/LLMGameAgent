from src import game_env
from src.game_bot import GameBot
from src.game_zork_training_test import run_training

done = True
DICT = "/media/jinming/Disk/Jinming/LLM/"
MODEL_NAME = DICT+"meta-llama/Meta-Llama-3.1-8B-Instruct"

def get_game_path(game_index = 0, game_name = ""):
    if game_name == "" and game_index == 0 :
        raise ValueError("No game selected!")

    game_path, game_types = game_env.get_game_by_index(game_index) if game_name == "" else game_env.get_game_by_name(game_name)
    if game_path == "" or game_types == game_env.GameType.none:
        raise ValueError(f"No game ({game_types.name}-{game_types.value}) environment is founded")

    return game_path, game_types

def get_game_env(game_index = 0, game_name = ""):
    game_path, game_types = get_game_path(game_index, game_name)

    return game_env.GameEnv(game_path)



def run_test():
    model = GameBot(MODEL_NAME) # loading LLM model
    game = get_game_env(1) # loading game env
    run_training(model, game)



if __name__ == "__main__":
    run_test()

