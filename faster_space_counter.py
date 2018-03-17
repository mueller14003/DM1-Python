def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]: sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

open_file = lambda n: list(map(lambda i: int(i.replace('\n','')),open(n,"r"))) #This lets you use your own file
spaces = lambda n: list(map(lambda i: n[i]-n[i-1],range(2,len(n)))) #Used 2 instead of 1 for lower range to ignore space between 2 and 3
count_spaces = lambda l: list(map(lambda n: [n,l.count(n)],sorted(list(dict.fromkeys(l)))))
# print(count_spaces(spaces(open_file("C:/Users/Kyle/mue14003/week07/first-ten-million-primes.txt")))) #You can modify your first 10 million primes file by removing everything but the numbers and changing the file extension to *.txt*
print(count_spaces(spaces(primes(100000))))
