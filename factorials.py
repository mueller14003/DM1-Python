from functools import *
from operator import mul

rfact = lambda n: n*rfact(n-1) if n>1 else n
mfact = lambda n: reduce(mul,range(1,n+1),1)

f = mfact(100000)
flen = len(str(f))
print(f)
print(flen)
