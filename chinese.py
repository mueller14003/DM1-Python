from functools import *
def egcd(a,b):
    if a==0:
        return (b,0,1)
    g,x,y = egcd(b%a,a)
    return (g,(y-(b//a)*x),x)

r,m = [4,2,9],[7,11,13]
mod = (m[0]*m[1]*m[2])
o,y = [mod//m[0],mod//m[1],mod//m[2]],[]
for i in range(0,3): y.append(egcd(o[i],m[i])[1])
top = 0
for i in range(0,3): top += (r[i]*o[i]*y[i])
result = top%mod
print(result)
#ind div
D = lambda mod,m: [mod//m[i] for i in range(len(m))]
#product list
P = lambda args: reduce(lambda x,y: x*y,args,1)
#find y
Y = lambda o,m: [egcd(o[i],m[i])[1] for i in range(len(m))]
#find top
T = lambda r,o,y: sum(r[i]*o[i]*y[i] for i in range(len(m)))

# def from_rns(r,m):
#     mod = P(m)
#     o = D(mod,m)
#     y = Y(o,m)
#     return top(r,o,y)%mod

# def FROM_RNS(r,m):
#     mod = 1
#     for i in m:
#         mod *= m
#     o = []
#     for i in m:
#         o.append(mod//m)
#     y = []
#     for i in range(0,len(m)):
#         y.append(egcd(o[i],m[i])[1])
#     top = 0
#     for i in range(0,len(m)):
#         top += (r[i]*o[i]*y[i])
#     return top%mod
#
# #m are the primes, r is the rns value thing


from_rns = lambda r,m: T(r,D(P(m),m),Y(D(P(m),m),m))%P(m)

print(from_rns([4,2,9],[7,11,13]))
