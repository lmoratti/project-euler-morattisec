from helper.problem import Problem 
import reuseful.reusable 


def solution_1():
    def eratosthenes_sieve(s) -> bytearray:
        p = bytearray([1]*s)
        for i in range(2,s):
            if p[i] == 1:
                for j in range(i,s):
                    if i * j < s:
                        p[i*j] = 0
                    else:
                        break
        return p
    n = 10001
    l = eratosthenes_sieve(n*12)
    p = []
    for idx,e in enumerate(l):
        if e == 1:
            p.append(idx)  

    return p[n+1]
    


problem = Problem(expected_answer=104743)
module  = __import__(__name__)
# #imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()