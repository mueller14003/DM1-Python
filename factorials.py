from functools import *
from operator import mul
import sys
sys.setrecursionlimit(10000)
import time

r=lambda n:n*r(n-1)if n>1else n
f=lambda n:0**n or n*f(n-1)
mfact = lambda n: reduce(mul,range(1,n+1),1)

t1 = time.time()
f1 = mfact(10000)
t2 = time.time()
print("Value: {}\nDigits: {}\nTime: {}".format(f1,len(str(f1)),t2-t1))
