# project-euler-morattisec
My solves for Project Euler. 

I also made a framework for evaluating the speed of the solutions for a given problem. Using a sample size of 1000 runs for each solution.

This allows dynamically importing multiple solutions that include "solution_" in their defined name.

Baseline for a new problem_x.py file:
```
from helper.problem import Problem 

def solution_1():
    # code here
    return answer
    
def solution_2():
    # code here
    return answer

def solution_3():
    # code here
    return answer

problem = Problem(expected_answer=0)
module  = __import__(__name__)
#imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()
```

Ouput:
```
[0.0010319000575691462, 0.0018933999817818403, 0.17959799990057945]
solution_2 was 1.8348675997190418x faster than previous result and was valid.
solution_3 was 94.85475949543604x faster than previous result and was valid.
solution_2 was 174.04592487731773x faster than the worst result (solution_1).
```