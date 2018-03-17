import numpy as np

def powers(m,n):
    return list(np.array(m)**n)

primes = lambda n : [x for x in range(2, n) if not 0 in map(lambda z : x % z, range(2, int(x**0.5+1)))]

def primePower(m,n):
    dict = {}
    for i in range(1,n+1):
        dict[i] = powers(primes(m),i)
    print(dict)

primePower(10,2)
