# Run main training loop here
from src import *
from src.game_env import GameEnv
from src.game_bot import GameBot
from src import relation_extraction


def run_training(model : GameBot, game_env : GameEnv):
    if game_env.done:
        game_env.initial_game()

    obs = game_env.get_current_observation()
    info = game_env.get_current_info()
    reward = game_env.get_current_reward()


    # Run main training loop
    while not game_env.done:
        # TODO: 28/10/2024 - Relation Extraction for building KG
        triple_vectors = relation_extraction.extract_relations_to_triple_vectors(obs)

        # TODO: 28/10/2024 - Update KG

        # TODO: 28/10/2024 - Check Act-Obj space / save previous succeeded Act-Obj pair to space.

        # TODO: 28/10/2024 - Pass matched Act-Obj pairs

        # TODO: 28/10/2024 - Check 'skill lib' for previous experiment based on obs and interactable objs with KG

        # TODO: 28/10/2024 - Merge previous experiment and possible actions to Thinking module.

        # TODO: 28/10/2024 - DO Action.

        # TODO: 28/10/2024 - !!How to Summarize experiment!!
    return