import itertools
def Cartesian_Product(*args):
    for i in itertools.product(*args):
        print(i)
Cartesian_Product(["a", "b", "c", "d"], [1, 2], ["x", "y", "z", "w", "t"], ["I", "am", "awesome"])
