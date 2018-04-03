from functools import *
f = lambda n: reduce(lambda x,y: x*y,range(1,n+1),1)
sin = lambda i,m=1000: sum([(-1)**n*i**(2*n+1)/f(2*n+1) for n in range(0,m+1)])
rad = lambda a: a*180.0/3.14159265358979323
print(sin(33))