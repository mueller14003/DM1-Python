from itertools import*
from decimal import*
getcontext().prec=1001
l=lambda n:int(''.join(str(len([*g]))+k for k,g in groupby(str(n))))
s=[1]
c=lambda n:[s.append(l(s[-1]))for _ in range(s[0],n+1)];c(100)
d=lambda ls,sd=1,n=100:[(ls[i])/ls[i-1]for i in range(1,n+1)]
print(*s)
print(*d(s))


# def lookandsay(n):
#     return ''.join(s(len([*g]))+k for k,g in groupby(s(n)))
# print(l(1234))


# Newman-Conway
# f=[0,1,1];q=lambda n:f[-1] if [f.append(f[f[i-1]]+f[i-f[i-1]])for i in range(3,n+1)] else 1;print(q(10))





