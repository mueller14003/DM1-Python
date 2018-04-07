#f=lambda n:n*f(n-1)if n>1else 1

# PI
# from decimal import*
# getcontext().prec=1001
# D=Decimal
# print(sum(D(16)^-k*(D(4)/(8*k+1)-D(2)/(8*k+4)-D(1)/(8*k+5)-D(1)/(8*k+6))for k in range(999)))

# EULER'S NUMBER
# import math,decimal
# decimal.getcontext().prec=1002
# print(str(sum(decimal.Decimal(1)/math.factorial(k)for k in range(999)))[:-1])

# PHI
# from decimal import*
# getcontext().prec=1001
# print((1+Decimal(5).sqrt())/2)

#n=0;exec('print(n);n=n+2^-(n^n+2)%3;'*25)

# for n in range(800):
#  if~bin(n).count('1')%2:print(n)
#[print(n)for n in range(800)if~bin(n).count('1')%2]
for i in range(1,101):
 n=''
 if not i%3:n+='Fizz'
 if not i%5:n+='Buzz'
 if n:print(n)
 else:print(i)