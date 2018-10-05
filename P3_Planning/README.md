Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/AIND-Planning). 
Udacity's README file is duplicated [here](README_Udacity.md).

## Method

The main goal of this project is to 

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

A detailed description of the results is contained in [heuristic_analysis.pdf](heuristic_analysis.pdf).
