import sys
from functools import *
from operator import mul
import math
sys.setrecursionlimit(10000)

rfact = lambda n: n*rfact(n-1) if n>1 else n
mfact = lambda n: reduce(mul,range(1,n+1),1)

f = mfact(100000)
#f = math.factorial(50000)
flen = len(str(f))
print(f)
print(flen)
