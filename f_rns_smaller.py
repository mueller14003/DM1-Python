from functools import *

egcd = lambda a,b: (lambda g,x,y: (g,y-(b//a)*x,x))(*egcd(b%a,a)) if a else (b,0,1) #lambda egcd recursive
ey = lambda o,m: egcd(o,m)[1] #Return Y value from egcd
mapc = lambda *n: list(map(n[0],*n[1:])) #mapcar*
P = lambda *n: reduce(lambda x,y: x*y,n,1) #product list
from_rns = lambda *n: sum(mapc(P,list(list(zip(*n))[1]),list(map(lambda x: reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)//x,list(list(zip(*n))[0]))),list(map(ey,list(map(lambda x: reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)//x,list(list(zip(*n))[0]))),list(list(zip(*n))[0])))))%reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)

print(from_rns((2,3),(3,1),(5,4)))