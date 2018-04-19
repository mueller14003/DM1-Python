#f=lambda n:n*f(n-1)if n>1else 1

# PI
# from decimal import*
# getcontext().prec=1001
# D=Decimal;o=D(1)
# print(sum(D(16)**-n*(4*o/(8*n+1)-o/(4*n+2)-o/(8*n+5)-o/(8*n+6))for n in range(999)))


# Just for fun
# l=10
# while 0>l>9:l=int(input("Length: "))
# s=str(int('1'*l)**2)
# [print('%{}s'.format(l-1)%s[:i-1]+s[-i:])for i in map(int,s)]

I=int
for i in map(I,'%s'%I('1'*9)**2):print(' '*(9-i),I('1'*i)**2)

# from decimal import*
# getcontext().prec=1001
# D=Decimal;o=D(1)
# print(sum((4*o/(8*k+1)-o/(4*k+2)-o/(8*k+5)-o/(8*k+6))/D(16)**k for k in range(999)))

# EULER'S NUMBER
# import math,decimal
# decimal.getcontext().prec=1002
# print(str(sum(decimal.Decimal(1)/math.factorial(k)for k in range(999)))[:-1])

# BETTER EULER'S NUMBER
# from decimal import*
# getcontext().prec=1001
# print(Decimal(1).exp())

# PHI
# from decimal import*
# getcontext().prec=1001
# print((1+Decimal(5).sqrt())/2)

# EVIL NUMBERS
# n=0;exec('print(n);n=n+2^-(n^n+2)%3;'*25)


# for i in range(1,101):
#  n=''
#  if not i%3:n+='Fizz'
#  if not i%5:n+='Buzz'
#  if n:print(n)
#  else:print(i)