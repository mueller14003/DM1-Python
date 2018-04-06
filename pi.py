#f=lambda n:n*f(n-1)if n>1else 1

# from decimal import*
# getcontext().prec=1001
# D=Decimal
# print(sum(D(16)**-k*(D(4)/(8*k+1)-D(2)/(8*k+4)-D(1)/(8*k+5)-D(1)/(8*k+6))for k in range(999)))

from math import*
from decimal import*
getcontext().prec=1002
D=Decimal
print(str(sum(D(1)/factorial(k)for k in range(999)))[:-1])