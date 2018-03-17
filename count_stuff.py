cool_dict = lambda n: {i:n.count(i) for i in list(dict.fromkeys(n))}
sort_dict = lambda n: {t[0]:t[1] for t in list(map(lambda key: [key,n[key]],sorted(n)))}
cool = cool_dict([3,5,9,10,12,13,5,3,2,7,1,2,3,2,1,12,20,18])
print(sort_dict(cool))
