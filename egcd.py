import sys
sys.setrecursionlimit(1000000)

def gcdr(a,b):
    r=a%b
    if r==0:
        return b
    elif r==1:
        return 1
    return gcdr(b,r)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

print(gcdr(1573428,567))
print(egcd(1573428,567))
print(xgcd(1573428,567))