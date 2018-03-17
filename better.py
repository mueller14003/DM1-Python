def better(b,p,m):
    r=1
    for i in range(1,p+1):
        r=(r*b)%m
    return r
print(better(2,3,11))
