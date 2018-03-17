mapcar = lambda func, values: list(map(func, values))
print(mapcar(lambda x: x**2, [1,2,3,4]))
