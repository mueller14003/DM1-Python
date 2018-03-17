import itertools

def shuffle(a):
    f = a[:int(len(a)/2)]
    last = a[int(len(a)/2):]
    return list(itertools.chain.from_iterable(zip(f,last)))

deck1 = ['Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','As','2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc']
deck2 = shuffle(deck1)
deck3 = shuffle(deck2)
deck4 = shuffle(deck3)
deck5 = shuffle(deck4)
deck6 = shuffle(deck5)
deck7 = shuffle(deck6)
deck8 = shuffle(deck7)
deck9 = shuffle(deck8)

if deck9 == deck1:
    print("Works")
else:
    print("Nope")
