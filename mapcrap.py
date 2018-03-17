a, b = [1, 2, 3], [4, 5, 6]


def map_for_some(a, b):
    def partial(x):
        return lambda y: y > a, x
    return list(filter(lambda i: partial(i), b))


print(map_for_some(a, b))
