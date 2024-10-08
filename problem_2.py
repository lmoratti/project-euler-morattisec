
from helper.problem import Problem 
''' 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 
1,2,3,5,8,13,21,34,55,89

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
def solution_1():
    
    f = [1,2]
    i = 1 # 2nd element
    s = 2
    while f[i] < 4000000:
        f.append(f[i] + f[i-1])
        i += 1 
        if f[i] % 2 == 0:
            s += f[i]
    print(s)
    return s
    
def solution_2():
    f = [1,2]
    i = 1 # 2nd element
    s = 2
    while f[i] < 4000000:
        f.append(f[i] + f[i-1])
        i += 3 
        s += f[i]
        
    return s

# def solution_3():
#     # code here
#     return answer

problem = Problem(expected_answer=0)
module  = __import__(__name__)
#imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()