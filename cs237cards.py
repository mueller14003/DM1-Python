from scipy.special import *

a = 10
r = 2
ways = 0

for i in range(2, 10):
    ways += comb(a,i)

print(ways)
