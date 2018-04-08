# p_list = []
# with open("C:/Users/Kyle/mue14003/week07/first-ten-million-primes.txt", "r") as f:
#     for line in f: p_list.append(int(line.replace('\n','')))
#
# isPrime = lambda n: n in p_list
#
def is_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i<1:return False
    return True

#Is_Prime = lambda n: False if n%i==0 for i in range(2,int(n**5)+1) else True
is_Prime = lambda n:all(n%i for i in range(2,int(n**.5)+1))
prime_list = lambda n:[i for i in range(2,n+1)if is_Prime(i)]
plist=lambda n:[print(i)for i in range(2,n+1)if all(i%j for j in range(2,i))]
printer = lambda n,f: [*map(print,f(n))]

printer(100,prime_list)
#plist(100)

# PI
# [print(n)for n in range(2,99)if all(n%i for i in range(2,n))]
# #[*map(print,list(iter(input,'.')))] #This is cool!! Though not related to prime numbers...

# Divisors
# r=range
#[print(*[i for i in r(1,n+1)if n%i<1])for n in r(1,101)]
