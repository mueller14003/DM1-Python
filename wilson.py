from math import *

def wilson(n):
    primes = []
    for i in range(2, n):
        if factorial(i - 1) % i == i - 1:
            primes.append("Prime: {}".format(i))
    print('\n'.join(primes))

wilson(5000)
