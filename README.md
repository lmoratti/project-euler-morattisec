# project-euler-morattisec
My solves for Project Euler. 

I also made a framework for evaluating the speed of the solutions for a given problem. Using a sample size of 1000 runs for each solution.

This allows dynamically importing multiple solutions that include "solution_" in their defined name.
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
[0.0019543999806046486, 0.0023890999145805836, 0.17309969989582896]
solution_2 was 1.222421171863422x faster than previous result and was valid.
solution_3 was 72.45393917575747x faster than previous result and was valid.
solution_2 was 88.56922923335054x faster than the worst result (solution_1).
```