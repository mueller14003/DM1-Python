is_prime = lambda n: False if False in list(map(lambda i: n%i,range(2,int(n**.5)+1))) else True
prime_list = lambda n: list(filter(lambda i: i if is_prime(i) else '',list(range(2,n+1))))

print(prime_list(100))

rle = [1,1,0,1,0,1,3,1,0,1,3,1,0,1,3,1,5,1,0,1,5,1,3,1,0,1,3,1,5,1,5,1,0,1,5,1,3,1,0,1,5,1,3,1,5,1,7,1,3]

def prime_list_from_rle_list(rle_list,limit):
    new_l,ran,c,primes = [],list(range(2,limit+1)),0,[]
    for j in rle_list:
        if j>1:
            for i in range(j):
                new_l.append((ran[c],0))
                c+=1
        else:
            new_l.append((ran[c],j))
            c+=1
    for i in new_l:
        if i[1]==1: primes.append(i[0])
    return primes

def test(rle):
    from_rle = prime_list_from_rle_list(rle,100)
    print(from_rle)
    if from_rle == prime_list(100): print("Works!")
    else: print("Fail")

test(rle)
