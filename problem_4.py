from helper.problem import Problem 
'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def solution_1():
    # code here

    def is_palindrome(n : int) -> bool:
        s = str(n)
        r = s[::-1]
        if s == r:
            return True
        return False
    
    s = set()
    for i in range(999,1,-1):
        for j in range(999,1,-1):
            if is_palindrome(i*j):
                s.add((i*j,i,j))
    
    l = sorted(list(s),key=lambda palindrome: palindrome[0])
    return l[-1][0]
    
# def solution_2():
#     # code here
#     return answer

# def solution_3():
#     # code here
#     return answer

problem = Problem(expected_answer=906609)
module  = __import__(__name__)

solution_1()
#imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()