from functools import *
from operator import mul
import math
import sys
sys.setrecursionlimit(10000)
import time

r=lambda n:n*r(n-1)if n>1else n
f=lambda n:0**n or n*f(n-1)
mfact = lambda n: reduce(mul,range(1,n+1),1)

t1 = time.time()
f1 = math.factorial(100000)
t2 = time.time()
print("Value: {}\nDigits: {}\nTime: {}".format(f1,len(str(f1)),t2-t1))


# make_f=lambda f:(lambda n:reduce(mul,range(n%len(f)or len(f),n+1,len(f)),1))if all(x=='!'for x in f)else lambda n:n
# call_f=lambda n,f:make_f(f)(n)
#
# n=make_f('wow')
# sf = make_f('!')
# df = make_f('!!')
# tf = make_f('!!!')
# qf=make_f('!!!!')


# print(sum(-df(abs(2*n-1))/sf(2*n+3)for n in range(0,1)))
