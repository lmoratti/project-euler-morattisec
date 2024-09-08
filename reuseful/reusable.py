''' 
Implmementations that might be helpful to reuse quickly.
'''
import random

def prime_factors(n: int) -> set:
    '''Return all prime factors'''
    if is_prime(n):
        return {n}
    else:
        all_factors = set()
        current = n

        while not is_prime(current):
            while True:
                d = pollards_rho(current)
                if d != n:
                    break

            all_factors = all_factors.union(prime_factors(d))
            current //= d

        all_factors.add(current)
        return all_factors


def gcd(a, b):
    ''' Return the greatest common divisor'''
    while b != 0: 
        b, a = a % b, b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def pollards_rho(n: int):
    ''' factorize n into n=pq'''
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
def linear_sieve(n):
    ''' find factorizations of all numbers, only use for n<10^7 numbers. O(n) '''
    lp = [0] * (n + 1)
    pr = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while i * pr[j] <= n:
            lp[i * pr[j]] = pr[j]
            if pr[j] == lp[i]:
                break
            j += 1
    return pr
            
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


def is_prime(n: int) -> bool:
    ''' Determines if a natural number is prime. Checks a cache of small primes, then uses miller-rabin with 64 iterations afterwards.'''
    small_primes = {2,3,5,7,11,13,17,19,23,29,31,37,41}

    if n in small_primes:
        return True

    for p in small_primes:
        if n % p == 0:
            return False
    return miller_rabin(n)

def miller_rabin(n, k=64):

        d = n - 1 
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        for _ in range(k):
            a = random.randint(2, n-2)
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