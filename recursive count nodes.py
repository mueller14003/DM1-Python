count = lambda n: 1 if n == 1 else 2*count(n/2)+1
print(count(4))