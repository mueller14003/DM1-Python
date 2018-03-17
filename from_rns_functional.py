from functools import *

egcd = lambda a,b: (lambda g,x,y: (g,y-(b//a)*x,x))(*egcd(b%a,a)) if a else (b,0,1) #lambda egcd recursive
ey = lambda o,m: egcd(o,m)[1] #Return Y value from egcd
mapc = lambda *args: list(map(args[0],*args[1:])) #mapcar*
P = lambda *args: reduce(lambda x,y: x*y,args,1) #product list
D = lambda mod,m: list(map(lambda x: mod//x,m)) #Integer division through list
Y = lambda o,m: list(map(ey,o,m)) #Get Y values of egcd for list
M = lambda *args: list(list(zip(*args))[0]) #Gives M values list
R = lambda *args: list(list(zip(*args))[1]) #Gives R values list
Mod = lambda *args: P(*M(*args))
gO = lambda *args: D(Mod(*args),M(*args)) #Givess O values list
gY = lambda *args: Y(gO(*args),M(*args)) #Gives Y values list
from_rns = lambda *args: sum(mapc(P,R(*args),gO(*args),gY(*args)))%Mod(*args)

print(from_rns((2,3),(3,1),(5,4)))

# T = lambda r,o,y: sum(list(map(P,r,o,y)))
# def from_rns(*args):
#     m,r,mod,o,y,top = list(list(zip(*args))[0]),list(list(zip(*args))[1]),1,[],[],0
#     mod = P(m)
#     o = D(mod,m)
#     y = Y(o,m)
#     top = T(r,o,y)
#     return top%mod

