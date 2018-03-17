input_text = input("Please enter desired text: ")

mktree = lambda n,i,r,p='': {'0':mktree(n,n[i][0],r,p+'0'),'1':mktree(n,n[i][1],r,p+'1')} if len(n[i]) == 2 else setr(i,r,p)

def setr(i,r,p=''):
    r[i] = p
    return i

def Huffman(_vals):
    vals,a1,a2,d = _vals.copy(),0,0,{}
    nodes = {n:[] for n in vals.keys()}
    while len(vals) > 1:
        s_vals = sorted(vals.items(),key=lambda x:x[1])
        a1,a2 = s_vals[0][0],s_vals[1][0]
        vals[a1+a2],nodes[a1+a2] = vals.pop(a1)+vals.pop(a2),[a1,a2]
    return d,mktree(nodes,a1+a2,d)

to_list = lambda s: list(map(lambda x: x,s))
to_string = lambda l: ''.join(l)
get_weight = lambda m: list(map(lambda i: (to_list(m).count(i),i),sorted(list(dict.fromkeys(to_list(m))))))
d,tree = Huffman({l:v for (v,l) in get_weight(input_text)})

def H_decode(d,message):
    de,id,m,c = [],dict(zip(d.values(),d.keys())),to_list(message),[]
    for i in m:
        c.append(i)
        if to_string(c) in d.values():
            de.append(id[to_string(c)])
            c = []
    return to_string(de)

H_encode = lambda d,m: to_string(list(map(lambda i: d[i],m)))

encoded = H_encode(d,input_text)
decoded = H_decode(d,encoded)
print("Dictionary: {}\nTree: {}\nEncoded: {}\nEncoded Hex: {}\nDecoded: {}".format(d,tree,encoded,hex(int(encoded,2)),decoded))
