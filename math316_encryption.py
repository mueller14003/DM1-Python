import numpy as np

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27}
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' '}

alphadec = lambda n: a.get(n, "Invalid Letter")
decalpha = lambda n: d.get(n, "Invalid number")
to_list = lambda e,k: seg_list(list(map(int,e.split(' '))),k,lambda n:n)
seg_list = lambda m,k,func: [func(m[i:i+len(k[0])]) for i in range(0,len(m),len(k[0]))]
dalist = lambda m: list(map(decalpha,m))
adlist = lambda m: list(map(alphadec,m))
fix_stuff = lambda n: list(map(lambda i: list(map(lambda j: int(j),i)),n))
to_str = lambda e: ' '.join([str(item) for i in e for item in i])
de_seg_list = lambda m: ''.join(dalist([item for i in m for item in i]))
dot_list = lambda l,k: list(map(lambda i: np.dot(k,i).tolist(),l))
encrypt = lambda m,k: to_str(dot_list(seg_list(m,k,adlist),k))
decrypt = lambda e,k: de_seg_list(dot_list(to_list(e,k),fix_stuff(np.linalg.inv(k).tolist())))

print(encrypt(" math rocks ", [[2,1,1],[3,2,1],[2,1,2]]))
print(decrypt("68 108 69 75 103 102 54 87 57 68 98 95",[[2,1,1],[3,2,1],[2,1,2]]))
