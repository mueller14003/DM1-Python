import numpy as np

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27}
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' '}

alphadec = lambda n: a.get(n, "Invalid Letter")
decalpha = lambda n: d.get(n, "Invalid number")
to_list = lambda e,k: seg_list(list(map(int,e.split(' '))),k,lambda n:n)
seg_list = lambda m,k,func: [func(m[i:i+len(k[0])]) for i in range(0,len(m),len(k[0]))]
dalist = lambda m: list(map(decalpha,m))
adlist = lambda m: list(map(alphadec,m))
make_list = lambda m=None,e=None: [[1 for i in range(0,int(len(list(m))**.5))] for j in range(0,int(len(list(m))**.5))] if m else [[1 for i in range(0,int(len(list(map(int,e.split(' '))))**.5))] for j in range(0,int(len(list(map(int,e.split(' '))))**.5))]
fix_stuff = lambda n: list(map(lambda i: list(map(lambda j: int(round(j)),i)),n))
to_str = lambda e: ' '.join([str(item) for i in e for item in i])
de_seg_list = lambda m: ''.join(dalist([item for i in m for item in i]))
encrypt = lambda m,k: to_str(np.matmul(seg_list(m,k,adlist),k))
decrypt = lambda e,k: de_seg_list(np.matmul(to_list(e,k),fix_stuff(np.linalg.inv(k).tolist())))
get_key = lambda m,e: fix_stuff(np.matmul(np.linalg.inv(seg_list(m,make_list(m=m),adlist)).tolist(),to_list(e,make_list(e=e))))

print(encrypt("decryptme", [[15, 4, 28], [16, 5, 20], [3, 1, 3]]))
print(decrypt("149 44 221 718 213 1052 523 150 835",[[15, 4, 28], [16, 5, 20], [3, 1, 3]]))
print(get_key("decryptme","149 44 221 718 213 1052 523 150 835"))
