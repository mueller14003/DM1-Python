from functools import *

m = [3,5,7]
egcd = lambda a,b: (lambda g,x,y: (g,y-(b//a)*x,x))(*egcd(b%a,a)) if a else (b,0,1) #lambda egcd
D = lambda mod,m: [mod//m[i] for i in range(len(m))] #ind div
P = lambda args: reduce(lambda x,y: x*y,args,1) #product list
Y = lambda o,m: [egcd(o[i],m[i])[1] for i in range(len(m))] #find y
T = lambda r,o,y: sum(r[i]*o[i]*y[i] for i in range(len(r))) #find top
from_rns = lambda r,m: T(r,D(P(m),m),Y(D(P(m),m),m))%P(m) #from rns
rns_list = [[1,1,3],[1,1,4],[1,4,3],[1,4,4],[2,1,3],[2,1,4],[2,4,3],[2,4,4]]
from_rns_dict = lambda rns: {from_rns(rns[i],m): rns[i] for i in range(0,len(rns))}
from_rns_list = lambda rns: [from_rns(rns[i],m) for i in range(0,len(rns))]
print(from_rns_dict(rns_list))
print(from_rns_list(rns_list))

list_mod = lambda l,m: [m**2%l[i] for i in range(0,len(l))]
mod_list = lambda l,m: [l[i]%m for i in range(0,len(l))]
