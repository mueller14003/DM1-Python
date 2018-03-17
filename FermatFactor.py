from math import *
def FermatFactor(N): # N should be odd
    a = ceil(sqrt(N))
    b2 = a*a - N
    while sqrt(b2) != int(sqrt(b2)):
        a = a + 1    # equivalently: b2 ← b2 + 2*a + 1
        b2 = a*a - N #               a ← a + 1
    return "{}, {}".format(a - sqrt(b2),a + sqrt(b2))

print(FermatFactor(125))
