from functools import *
num_f = lambda csf: reduce(lambda x,y: x*y,list(map(lambda i: csf[i][1]+1,range(0,len(csf)))),1)
print(num_f([[2,3],[3,1],[5,2]]))