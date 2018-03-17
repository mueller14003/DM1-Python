from math import *

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def isSquareFree(n):
    for i in range(2,int(sqrt(n))+1):
        for j in range(2,10):
            if n % (i**j) == 0:
                return False
    return True

def prime_list(n):
    prime = []
    for i in range(2,n+1):
        if isPrime(i):
            prime.append(i)
    return prime

plist = prime_list(20)
print(plist)

def PrimeBaseTwoDec(n,p):
    bin = 1
    out = 0
    for i in p:
        if n % i == 0:
            out += bin
        bin *= 10
    return int(str(out),2)

def twostuff(n):
    cool = []
    count = 0
    cool.append("\n  | Squarefree Number | Nonnegative Integer |\n  |-+-|")
    for i in range(1, n+1):
        if i == 1:
            cool.append("  | {} | {} |".format(i,0))
        if isPrime(i) and i != 1:
            cool.append("  | {} | {} |".format(i,2**count))
            count += 1
        if isSquareFree(i) and not isPrime(i):
            cool.append("  | {} | {} |".format(i,PrimeBaseTwoDec(i,plist)))
    print('\n'.join(cool))

twostuff(42)