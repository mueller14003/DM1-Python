from math import *
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def coolPrimes(n):
    count = 0
    for i in range(10**(n-1),10**n+1):
        if isPrime(i):
            if sqrt(i-1) == int(sqrt(i-1)):
                count += 1
                print("prime: {}, n: {}, count: {}".format(i,int(sqrt(i-1)),count))
    print("There are {} primes of {} digits that have the form n^2 + 1.".format(count,n))

coolPrimes(7)
