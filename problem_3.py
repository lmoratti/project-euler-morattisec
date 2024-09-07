from helper.problem import Problem 
'''The prime factors of 13195 are 5,7,13 and 29. 

What is the largest prime factor of the number 600851475143?
'''
def solution_1():

    # crappy is prime
    def is_prime(n: int) -> bool:
        for i in range(2, int(n ** (1/2) +1)):
            if n % i == 0:
                return False
        return True
    f=0
    n = 600851475143
    for i in range(int(n ** (1/2)), 2, -1): #descend the range to find greatest factor first, divide by 2 to shorten range
        if n % i == 0: # is a factor
            if is_prime(i): # is also prime
                f = i
                break
    
    print(f)
    return f
    
# def solution_2():
#     # code here
#     return answer

# def solution_3():
#     # code here
#     return answer
solution_1()
# problem = Problem(expected_answer=0)
# module  = __import__(__name__)
# imports all functions that are named "solution_*"
# problem.import_solutions(module)
# problem.time_solve()
# problem.announce_results()