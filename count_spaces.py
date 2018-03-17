open_file = lambda n: list(map(lambda i: int(i.replace('\n','')),open(n,"r"))) #This lets you use your own file
is_prime = lambda n: False if False in list(map(lambda i: n%i,range(2,int(n**.5)+1))) else True
prime_list = lambda n: list(filter(lambda i: i if is_prime(i) else '',range(2,n+1)))
spaces = lambda n: list(map(lambda i: n[i]-n[i-1],range(2,len(n)))) #Used 2 instead of 1 for lower range to ignore space between 2 and 3
count_spaces = lambda l: list(map(lambda n: [n,l.count(n)],sorted(list(dict.fromkeys(l)))))
print(count_spaces(spaces(open_file("C:/Users/Kyle/mue14003/week07/first-ten-million-primes.txt")))) #You can modify your first 10 million primes file by removing everything but the numbers and changing the file extension to *.txt*
