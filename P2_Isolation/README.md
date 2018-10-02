Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/AIND-Isolation). 
Udacity's README file is duplicated [here](README_Udacity.md).

![Example game of isolation](viz.gif)

## Method

The main goal of this project is to build an adversarial search agent that plays the game of isolation.
This particular version of uses pieces that move in an L shape, like knights in chess. An example game is shown above.
As the pieces move, the squares they leave are removed from the board; i.e., they may no longer be moved to.
The first player that can't move to an open square loses.

Adversarial search is a type of heuristic search that is typically used in games where the players oppose each other.
The search algorithm takes into account whether each node in the search tree leads towards victory or defeat based on an evaluation function.

In this project, three such algorithms are explored: random, [Minimax](https://en.wikipedia.org/wiki/Minimax) and [Alpha-Beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

A description of the files in this repository follows:


Notes | File | Usage
-- |  --- | ---
[2] | [isolation/isolation.py](isolation/isolation.py) | Provides the Board class |
[1] | [game_agent.py](game_agent.py) | My implementation of the Minimax and AlphaBeta algorithms |
[1] | [play1game.py](play1game.py) | My implementation of a single game execution for debugging |
[2] | [sample_players.py](sample_players.py) | provides sample player classes and eval functions for tournament.py |
[2] | [tournament.py](tournament.py) | pits the various players against each other over many games for heuristic evaluation |
[1] | [heuristic_analysis.pdf](heuristic_analysis.pdf) | Student analysis comparing performance of the three algorithms |
[1] | [research_review.pdf](research_review.pdf) | Student summary of research paper on Deep Blue (ref. within) |

- [1] Implemented by the student using supplied sample/skeleton code
- [2] Supplied


## Results

