input_text = input("Please enter desired text: ")

mktree = lambda n,i,r,p='': {'0':mktree(n,n[i][0],r,p+'0'),'1':mktree(n,n[i][1],r,p+'1')} if len(n[i]) == 2 else setr(n,i,r,p)

def setr(n,i,r,p=''):
    r[i] = p
    return i

def Huffman(_vals):
    vals,a1,a2 = _vals.copy(),0,0
    nodes = {n:[] for n in vals.keys()}
    while len(vals) > 1:
        s_vals = sorted(vals.items(),key=lambda x:x[1])
        a1,a2 = s_vals[0][0],s_vals[1][0]
        vals[a1+a2],nodes[a1+a2] = vals.pop(a1)+vals.pop(a2),[a1,a2]
    d,root = {},a1+a2
    tree = mktree(nodes,root,d)
    return d,tree

to_list = lambda s: list(map(lambda x: x,s))
to_string = lambda l: ''.join(l)
get_weight = lambda m: list(map(lambda i: (to_list(m).count(i),i),sorted(list(dict.fromkeys(to_list(m))))))
d,tree = Huffman({l:v for (v,l) in get_weight(input_text)})

def H_decode(d,message):
    decoded,id,m,current = [],dict(zip(d.values(),d.keys())),to_list(message),[]
    for i in m:
        current.append(i)
        if to_string(current) in d.values():
            decoded.append(id[to_string(current)])
            current = []
    return to_string(decoded)

H_encode = lambda d,m: to_string(list(map(lambda i: d[i],m)))

print("Dictionary:",d)
print("Tree:",tree)
encoded = H_encode(d,input_text)
print("Encoded:",encoded)
print("Encoded Hex:",hex(int(encoded,2)))
decoded = H_decode(d,encoded)
print("Decoded:",decoded)