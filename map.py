p,q = 3,5
pl = lambda p,q: list(map(lambda n: n%p,list(range(0,p*q))))
ql = lambda p,q: list(map(lambda n: n%q,list(range(0,p*q))))
table = lambda p,q: list(map(lambda i: "| {} | {} | {} |".format(i,pl(p,q)[i],ql(p,q)[i]),range(0,p*q)))
print('\n'.join(table(p,q)))