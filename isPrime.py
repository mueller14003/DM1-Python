# p_list = []
# with open("C:/Users/Kyle/mue14003/week07/first-ten-million-primes.txt", "r") as f:
#     for line in f: p_list.append(int(line.replace('\n','')))
#
# isPrime = lambda n: n in p_list
#
def is_prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0: return False
    return True

#Is_Prime = lambda n: False if n%i==0 for i in range(2,int(n**5)+1) else True
def nothing(): pass
is_Prime = lambda n: False if False in list(map(lambda i: n%i,range(2,int(n**.5)+1))) else True
prime_list = lambda n: list(filter(lambda i: i if is_prime(i) else nothing(),list(range(2,n+1))))
printer = lambda n,f: [*map(print,f(n))]

#printer(100,prime_list)

#[print(n)for n in range(2,99)if all(n%i for i in range(2,n))]
#[*map(print,list(iter(input,'.')))] #This is cool!! Though not related to prime numbers...
r=range
[print(*[str(i)for i in r(1,n+1)if n%i==0])for n in r(1,101)]
# [*map(lambda n:print(*map(str,filter(lambda i:n%i==0,r(1,n+1)))),r(1,101))]