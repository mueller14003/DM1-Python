from decimal import*
getcontext().prec=1001
D=Decimal
print(sum(1/D(16)**k*(D(4)/(8*k+1)-D(2)/(8*k+4)-D(1)/(8*k+5)-D(1)/(8*k+6))for k in range(999)))