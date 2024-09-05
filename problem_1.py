from helper.problem import Problem 
import itertools

# Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6,and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1,000.

def solution_1():
    ''' This solution is O(n) '''
    def is_multiple_of(number: int, multiples: list) -> bool:
        for term in multiples:
            if number % term == 0:
                return True
        return False

    sum: int  = 0
    multiples = [3, 5]

    for number in range(1,1000):
        if is_multiple_of(number, multiples):
            sum += number
    return sum
    
def solution_2():
    ''' This solution is O(M) '''
    def sum_range_with_multiple(n: int, m: int) -> int:
        e  = (n - 1) // m
    
        return (e ** 2 + e ) // 2 * m

    sum: int  = 0
    multiples = [3, 5]
    n = 1000

    for m in multiples:
        sum += sum_range_with_multiple(n, m)

    sum -= sum_range_with_multiple(n, (multiples[0] * multiples[1]) )

    return sum

def solution_3():
    def sum_range_with_multiple(n: int, m: tuple) -> int:
        r = 1
        for i in m:
            r *= i
        e  = (n - 1) // r
        return (e ** 2 + e ) // 2 * r
    
    n = 1000
    B = [3, 5]
    s = 0

    for i in range(1, len(B)+ 1) :
        for c in itertools.combinations(B, i):
            s += (-(-1) ** i )* sum_range_with_multiple(n, c)
    return s


problem = Problem(expected_answer=233168)
module  = __import__(__name__)
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()


