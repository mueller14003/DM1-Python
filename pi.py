fact = lambda n: n*fact(n-1) if n > 1 else 1
calc_pi = lambda n: (12/(640320*(640320**.5)))*sum(list(map(lambda k: (((-1)**k)*fact(6*k)*(13591409+(545140134*k)))/(fact(3*k)*(fact(k)**3)*640320**(3*k)),range(0,n+1))))
print(format(1/calc_pi(1),'.100f'))

