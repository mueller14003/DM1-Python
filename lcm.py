from functools import *
def gcdr(a,b):
    r=a%b
    if r==0:
        return b
    elif r==1:
        return 1
    return gcdr(b,r)
def lcm(a,b):
    return (a*b)/gcdr(a,b)
def lcmr(args):
    s = 1
    for i in args:
        s = lcm(i,s)
    return s
def print_cool(*args):
    print("{} <--> ( {})".format(args[0],unpack(args[0],args[1:])))
def unpack(i,rest):
    string = ""
    for j in rest:
        string += "{} ".format(i%j)
    return string
def RMOD(*args):
    print("MOD with redundancies:")
    for i in range (0,reduce(lambda x, y: x*y, args, 1)+1):
        print_cool(i,*args)
def MOD(*args):
    print("MOD without redundancies:")
    for i in range(0,int(lcmr(args)+1)):
        print_cool(i,*args)

RMOD(3,5,8,4,6)
MOD(3,5,8,4,6)