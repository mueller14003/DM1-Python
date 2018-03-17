import itertools
a, b = ["A", "B", "C"], ["x", "y", "z"]
print(list(itertools.chain.from_iterable(zip(a, b))))
