from helper.problem import Problem 
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def solution_1():
    def is_evenly_divisible(n: int, r:range):
        for i in r:
            if not n % i == 0:
                return False
        return True

    i = 1
    while True:
        if is_evenly_divisible(i,range(1,20)):
            break
        else:
            i += 1
    print(i)
    return i
    
# def solution_2():
#     # code here
#     return answer

# def solution_3():
#     # code here
#     return answer
solution_1()
# problem = Problem(expected_answer=0)
# module  = __import__(__name__)
# #imports all functions that are named "solution_*"
# problem.import_solutions(module)
# problem.time_solve()
# problem.announce_results()