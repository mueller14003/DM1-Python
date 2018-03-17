from functools import *

m = [7,11,13]
egcd = lambda a,b: (lambda g,x,y: (g,y-(b//a)*x,x))(*egcd(b%a,a)) if a else (b,0,1) #lambda egcd recursive
D = lambda mod,m: [mod//m[i] for i in range(len(m))] #ind div
P = lambda args: reduce(lambda x,y: x*y,args,1) #product list
Y = lambda o,m: [egcd(o[i],m[i])[1] for i in range(len(m))] #find y
T = lambda r,o,y: sum(P([r[i],o[i],y[i]]) for i in range(len(r))) #find top
to_rns = lambda *args: [args[0]%i for i in args[1:]] #to rns without list
from_rns = lambda r,m: T(r,D(P(m),m),Y(D(P(m),m),m))%P(m) #from rns without list
rns_dict = lambda *args: {i: to_rns(i,*args) for i in range(0,P(args))} #creates rns dictionary
dict = rns_dict(*m) #rns dictionary
d_to_rns = lambda n: dict[n] #to rns with dictionary
d_from_rns = lambda n: list(dict.keys())[list(dict.values()).index(n)] #from rns with dictionary
add_rns = lambda a,b,m: [(a[i]+b[i])%m[i] for i in range(0,len(m))]
mul_rns = lambda a,b,m: [(a[i]*b[i])%m[i] for i in range(0,len(m))]

print(from_rns([2,9,9],m))

def test(n,b):
    print("n = {}, b = {}".format(n,b))
    print("rns(n) =",d_to_rns(n))
    print("from_rns(rns(n)) =",d_from_rns(d_to_rns(n)))
    print("add_rns(rns(n),rns(b)) =",add_rns(d_to_rns(n),d_to_rns(b),m))
    print("from_rns(add_rns(rns(n),rns(b))) =",d_from_rns(add_rns(d_to_rns(n),d_to_rns(b),m)))
    print("mul_rns(rns(n),rns(b)) =",mul_rns(d_to_rns(n),d_to_rns(b),m))
    print("from_rns(mul_rns(rns(n),rns(b))) =",d_from_rns(mul_rns(d_to_rns(n),d_to_rns(b),m)))

test(9,20)
