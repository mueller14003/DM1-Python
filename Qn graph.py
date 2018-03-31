Table = lambda n: [['i','nodes','edges']] + list(map(lambda i:[i,2**i,i*2**(i-1)],range(0,n+1)))
[print(x) for x in Table(10)]