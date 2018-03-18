input_text = input("Please enter desired text: ")
mktree = lambda n,i,r,p='': {'0':mktree(n,n[i][0],r,p+'0'),'1':mktree(n,n[i][1],r,p+'1')} if len(n[i]) == 2 else setr(i,r,p)
def setr(i,r,p):
    r[i] = p
    return i
def Huffman(_vals):
    vals,a1,a2,d,nodes = _vals.copy(),0,0,{},{n:[] for n in _vals.copy().keys()}
    while len(vals) > 1:
        a1,a2 = sorted(vals.items(),key=lambda x:x[1])[0][0],sorted(vals.items(),key=lambda x:x[1])[1][0]
        vals[a1+a2],nodes[a1+a2] = vals.pop(a1)+vals.pop(a2),[a1,a2]
    return d,mktree(nodes,a1+a2,d)
get_weight = lambda m: list(map(lambda i: (list(map(lambda x: x,m)).count(i),i),sorted(list(dict.fromkeys(list(map(lambda y: y,m)))))))
d,tree = Huffman({l:v for (v,l) in get_weight(input_text)})
H_encode = lambda d,m: ''.join(list(map(lambda i: d[i],m)))
def H_decode(d,message):
    de,id,m,c = [],dict(zip(d.values(),d.keys())),list(map(lambda x: x,message)),[]
    for i in m:
        c.append(i)
        if ''.join(c) in d.values():
            de.append(id[''.join(c)])
            c = []
    return ''.join(de)
print("Dictionary: {}\nTree: {}\nEncoded: {}\nEncoded Hex: {}\nDecoded: {}".format(d,tree,H_encode(d,input_text),hex(int(H_encode(d,input_text),2)),H_decode(d,H_encode(d,input_text))))
