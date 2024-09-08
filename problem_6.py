from helper.problem import Problem 
''' 
The sum of the squares of the first ten natural numbers is,

    1 ** 2 , 2 ** 2 , .... 10 **  = 385
The square of the sum of the first ten natural numbers is,
    ( 1 + 2 + 3 ... 10) ** 2 = 55 ** 2 = 3025


Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def solution_1():
    ''' This solution is O(1)'''
    def sum_of_the_squares(n : int) -> int:
        # Gauss Diagonalised adding trick for first n natural numbers to the power of 2
        return n*(n+1)*(2*n + 1)/6
    def square_of_the_sum_of_range(a: int, b : int)-> int:
        s = ((a + b) * (b - a + 1)) /2 
        return s ** 2
    
    a = sum_of_the_squares(100)
    b = square_of_the_sum_of_range(1,100)
    d = b - a 
    return d




problem = Problem(expected_answer=25164150)
module  = __import__(__name__)
# imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()