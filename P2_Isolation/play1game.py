import itertools
import random
import warnings

from collections import namedtuple

from isolation import Board
from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
                        custom_score_2, custom_score_3)

TIME_LIMIT = 300  # number of milliseconds before timeout

Agent = namedtuple("Agent", ["player", "name"])


def play_round(cpu_agent, test_agent):

    game = Board(cpu_agent.player, test_agent.player)

    # initialize all games with a random move and response
#    for _ in range(2):
#        move = random.choice(game.get_legal_moves())
#        game.apply_move(move)

    # play all games and tally the results
    winner, move_history, termination = game.play(time_limit=TIME_LIMIT)

    print (winner,move_history,termination)

def main():

    # Define two agents to compare -- these agents will play from the same
    # starting position against the same adversaries in the tournament
    test_agent = \
        Agent(AlphaBetaPlayer(score_fn=custom_score_2), "AB_Custom_2")
#        Agent(AlphaBetaPlayer(score_fn=improved_score), "AB_Improved"),
#        Agent(AlphaBetaPlayer(score_fn=custom_score), "AB_Custom")
#        Agent(AlphaBetaPlayer(score_fn=custom_score_3), "AB_Custom_3")


    # Define a collection of agents to compete against the test agents
    cpu_agent = \
        Agent(MinimaxPlayer(score_fn=center_score), "MM_Center")
#        Agent(MinimaxPlayer(score_fn=open_move_score), "MM_Open")
#        Agent(RandomPlayer(), "Random"),
#        Agent(MinimaxPlayer(score_fn=improved_score), "MM_Improved"),
#        Agent(AlphaBetaPlayer(score_fn=open_move_score), "AB_Open"),
#        Agent(AlphaBetaPlayer(score_fn=center_score), "AB_Center"),
#        Agent(AlphaBetaPlayer(score_fn=improved_score), "AB_Improved")

    play_round(cpu_agent, test_agent)


if __name__ == "__main__":
    main()
