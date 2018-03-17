to_list = lambda s: list(map(lambda i: i, s))
to_string = lambda l: ''.join(l)

def H_decode(d,message):
    decoded,id,m,current = [],dict(zip(d.values(),d.keys())),to_list(message),[]
    for i in m:
        current.append(i)
        if to_string(current) in d.values():
            decoded.append(id[to_string(current)])
            current = []
    return to_string(decoded)

H_encode = lambda d,m: to_string(list(map(lambda i: d[i],m)))

print(H_encode({'f':'000','i':'001','s':'010','h':'011','r':'100','t':'101','e':'11'},'ifheresetthere'))
print(H_decode({'f':'000','i':'001','s':'010','h':'011','r':'100','t':'101','e':'11'},'0010000111110011010111011010111110011'))
