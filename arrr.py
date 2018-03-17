from math import *

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

is_prime = lambda n: False if False in [n%i!=0 for i in range(2,int(sqrt(n)+1))] else True

print(is_prime(101))

def getsmallp(n):
    pairs = []
    i = 1
    while i <= n:
        for j in range(i ** 2, (i + 1) ** 2 + 1):
            if i ** 2 < j < (i + 1) ** 2 and isPrime(j):
                pairs.append("({} {})".format(i, j))
                i += 1
    return pairs

# stuff = getsmallp(100)
# print('\n'.join(stuff))