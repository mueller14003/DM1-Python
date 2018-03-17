from functools import *
egcd = lambda a,b: (lambda g,x,y: (g,y-(b//a)*x,x))(*egcd(b%a,a)) if a else (b,0,1) #lambda egcd recursive
ey = lambda o,m: egcd(o,m)[1] #Return Y value from egcd
mapc = lambda *n: list(map(n[0],*n[1:])) #mapcar*
P = lambda *n: reduce(lambda x,y: x*y,n,1) #product list
from_rns = lambda *n: sum(mapc(P,list(list(zip(*n))[1]),list(map(lambda x: reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)//x,list(list(zip(*n))[0]))),list(map(ey,list(map(lambda x: reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)//x,list(list(zip(*n))[0]))),list(list(zip(*n))[0])))))%reduce(lambda x,y: x*y,list(list(zip(*n))[0]),1)

def find_stuff(m):
    cool = []
    for i in range(0,1000):
        i_str = str(i)
        if len(str(i)) < 3:
            if len(i_str) == 1: i_str = "00"+i_str
            else: i_str = "0"+i_str
        ilist = [int(x) for x in i_str]
        frns = from_rns(*list(zip(m,ilist)))
        # print(list(zip(m, ilist)),"frns = {}, i = {}".format(frns,i))
        if frns == i:
            cool.append(i)
    return cool

print(find_stuff([7,11,13]))
