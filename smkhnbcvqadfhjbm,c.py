from math import *

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def findC(b,t,r):
    c = [0,0]
    for i in range(b,t):
        m = [(i * 2 - 1),0]
        sweetness = 0
        for x in range(r):
            if isPrime(x**2 + x + m[0]):
                sweetness += 1
        m[1] = sweetness
        if m[1] > c[1]:
            c = m
    return c

print(findC(1,2000,1000))
