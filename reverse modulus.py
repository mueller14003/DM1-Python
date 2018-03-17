def reverse_modulo(a,b,c):
    n = 1
    while True:
        if n % 7 == a and n % 11 == b and n % 13 == c:
            return n
        else:
            n += 1

print(reverse_modulo(2,1,9))