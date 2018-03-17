is_prime = lambda n: False if False in [n%i != 0 for i in range(2,int(n**.5)+1)] else True


# def IsPrime(n):
#     for i in range(2,int(n**.5)+1):
#         if n%i == 0:
#             return False
#     return True