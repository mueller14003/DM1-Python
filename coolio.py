def prime_list(n):
  prime = []
  for i in range(2,n+1):
    is_prime = True
    for j in range(2,i//2+1):
      if i % j == 0:
        is_prime = False
    if is_prime:
      prime.append(i)
  return prime

def primePower(l,p):
  c = 0
  cool = []
  for i in l:
    cool.append(p[c]**i)
    c += 1
  return cool

def product(l):
  p = 1
  for i in l:
    p *= i
  return p

p = prime_list(100)
l = [0, 1, 2, 0, 0, 0, 0, 0, 1]
pp = primePower(l,p)
print(product(pp))
