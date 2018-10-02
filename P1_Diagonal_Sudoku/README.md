Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/aind-sudoku). 
Udacity's README file is duplicated [here](README_Udacity.md).

## Method

The main goal of this project is to build an intelligent agent that will solve every sudoku while introducing two powerful techniques that are used throughout the field of AI: constraint propagation and search.

Student solutions are found in [solution.py](solution.py). The core of the algorithm is a depth-first search found in the "search" function. The first thing "search" does is to apply constraints to the existing puzzle using the "reduce_puzzle" function. That function in turn applies as many constraints as can be imagined to eliminate possibilities. The more constraints that can be applied, the quicker the board is solved.

Once that is done, the "search" function picks the box with the least number of possible values, and iterates over the possible values, constructing a new sudoku for each one and recursively calling "search" on that new sudoku board. If that branch of the search tree finds a solution, the game is over, else it keeps searching.

After the board is solved, the program visualizes the history of the number placement.

## Results

