def gcd(a,b):
    g = 1
    for i in range(2,b+1):
        if (a%i==0) and (b%i==0): g=i
    return g

def lcm(a,b):
    for i in range(1,a*b+1):
        if (i % a == 0) and (i % b == 0):
            return i

for i in range(1,20):
    for j in range(1,20):
        if i > j:
            print("gcd*lcm:",(gcd(i,j) * lcm(i,j)))
            print("a*b:",i*j)
            if (gcd(i,j) * lcm(i,j)) == (i*j):
                print("Equiv\n")
            else:
                print("Not")