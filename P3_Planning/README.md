Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/AIND-Planning). 
Udacity's README file is duplicated [here](README_Udacity.md).

## Method

The main goal of this project was to learn AI planning concepts by implementing a logistics planning system in the air cargo domain, in which three types of objects are relevant: planes, airports, and cargo. Concepts covered include various search algorithms, experimenting with different heuristic functions, and planning graphs.

Three problems were defined with initial and goal states; the completion of the problem was defined as reaching the goal of having the cargos unloaded at their destination airports:

1. 2 each of planes (P1,P2), airports (JFK,SFO) and cargo (C1,C2)
1. 3 each of planes (P1,P2,P3), airports (JFK,SFO,ATL) and cargo (C1,C2,C3)
1. 2 planes (P1,P2), 4 each of airports (JFK,SFO,ATL,ORD) and cargo(C1,C2,C3,C4)

Each of these problems was to be solved using several search algorithms and heuristics, divided as follows. First, a collection of so-called "uninformed" search algorithms:

1. breadth_first_search
1. breadth_first_tree_search
1. depth_first_graph_search
1. depth_limited_search
1. uniform_cost_search
1. recursive_best_first_search with no heuristic
1. greedy_best_first_graph_search with no heuristic
1. astar_search with no heuristic

Second, a collection of informed search algorithms with heuristics:

1. astar_search with "ignore_preconditions" heuristic
1. astar_search with "levelsum" heuristic for the planning graph solver

Subsequently, an analysis was to be performed of the comparative efficiency of the solutions as well as the speed of convergence to a solution.

A description of the files in this repository follows:

Notes | File | Usage
--- |  --- | ---
[2] | [aimacode/logic.py](aimacode/logic.py) | base class "KB" (knowledge base of logical expressions), derived classes, and logic operations 
[2] | [aimacode/planning.py](aimacode/planning.py) | class Action - defines actions to be taken as logical expressions with preconditions and effects 
[2] | [aimacode/search.py](aimacode/search.py) | base class Problem, class Node (of a search tree), all search algo implementations 
[2] | [aimacode/utils.py](aimacode/utils.py) | class Expr (logical expression class) and many utility functions 
[2] | [lp_utils.py](lp_utils.py) | class FluentState, converts state information (collection of boolean variables) to strings, e.g., "TFFTFF" and vice versa 
[2] | [run_search.py](lp_utils.py) | main routine (`python run_search.py`), presents text menu to the user of problems to run 
[1] | [my_air_cargo_problems.py](my_air_cargo_problems.py) | class AirCargoProblem derived from base class Problem, contains state information for planes, airports and cargo, and a list of all possible actions (e.g., Load cargo C1 on plane P1 at airport A1) 
[1] | [my_planning_graph.py](my_planning_graph.py) | class PlanningGraph and support classes, student implemented build graph support functions and consistency check functions 
[1] | [heuristic_analysis.pdf](heuristic_analysis.pdf) | My analysis comparing performance of the three algorithms 
[1] | [research_review.pdf](research_review.pdf) | My summary of a survey paper on AI planning systems research 

- [1] Implemented by the student using supplied sample/skeleton code
- [2] Supplied


## Results

A detailed description of the results, including tables and graphs, is contained in [heuristic_analysis.pdf](heuristic_analysis.pdf). The "executive summary" is as follows:

1. Most of the algorithms could find optimal solutions, but with widely varying efficiencies.
1. The number of "node expansions" during the tree search was a pretty accurate predictor of the total execution time, and the informed (heuristic) searches were best at limiting the number of node expansions, particularly as the problem got more complex.
1. The notable exception to this rule of thumb was the "levelsum" heuristic for the planning graph solver. Creating a new planning graph at each node more than offset the efficient search, meaning that the execution time was worse even than several uninformed searches.

