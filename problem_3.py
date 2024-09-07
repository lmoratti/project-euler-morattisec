from helper.problem import Problem 
import time
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

    return f
    
def solution_2():
       # pollards rho
    def thanks_mr_pollard(n: int):
        # based gcd
        def gcd(a, b):
            while b != 0: 
                b, a = a % b, b
            return a

        def g(x: int):
            return (x ** 2 +1) % n
        
        x = 2
        y = x
        d = 1

        while d ==1:
            x = g(x)
            y = g(g(y))
            d = gcd(abs(x - y), n)

        return d
    
    class Random:
        def __init__(self) -> None:
            self.state = int(time.time())
            # ANSI C
            self.a = 1103515245
            self.c = 12345
            self.m = 2 ** 31

        def generate(self):
            ''' https://en.wikipedia.org/wiki/Linear_congruential_generator'''

            self.state = (self.a*self.state +self.c ) % self.m
            return self.state
        
        def get_bits(self, k):
            if k < 0:
                raise ValueError

            b = (self.m - 1).bit_length()
            c = (k + (b-1)) // b  
            n = 0

            for _ in range(c):
                n <<= b
                n += self.generate()

            return n % 2**k
        
        def random_int(self, n: int):
            k = n.bit_length()
            while True:
                m = self.get_bits(k)
                if m < n:
                    return m
        
        def random_int_between(self, l, u):
            return self.random_int(u-l) + l


    def miller_rabin(n, k=64):
        r = Random() 
        d = n - 1 
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        for _ in range(k):
            a = r.random_int_between(2, n-2)
            # x = a ** d % n
            x = pow(a, d, n)
            for _ in range(s):
                y = pow(x,2,n)
                if y == 1 and x != 1 and x != n - 1:
                    return False
                x = y
            if y != 1:
                return False
        return True

    
    def is_prime(n: int) -> bool:
        small_primes = {2,3,5,7,11,13,17,19,23,29,31,37,41}

        if n in small_primes:
            return True

        for p in small_primes:
            if n % p == 0:
                return False
        return miller_rabin(n)


    def factor(n: int):
        if is_prime(n):
            return {n}
        else:
            all_factors = set()
            current = n

            while not is_prime(current):
                while True:
                    d = thanks_mr_pollard(current)
                    if d != n:
                        break

                all_factors = all_factors.union(factor(d))
                current //= d

            all_factors.add(current)
            return all_factors
        
    n = 600851475143
    s = factor(n)
    l = sorted(list(s))
    return l[-1]


    
problem = Problem(expected_answer=6857)
module  = __import__(__name__)
#imports all functions that are named "solution_*"
problem.import_solutions(module)
problem.time_solve()
problem.announce_results()