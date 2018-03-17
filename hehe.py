from math import *
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def allComp(n):
  for i in n:
    if isPrime(i):
      return False
  return True

comp = [39916802, 39916803, 39916804, 39916805, 39916806, 39916807, 39916808, 39916809, 39916810, 39916811]
print(allComp(comp))