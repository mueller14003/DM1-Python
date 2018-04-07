# v=adv=art=adj=n=2
# np=(art*adj*n)+(art*n)
# vp=(v*adv)+v
# s=(np*vp*np)+(np*vp)
# print(s)
# from functools import*
# P=lambda l:reduce(lambda x,y:x*y,l,1)
# pf=lambda m,l:[P([*map(lambda x,y:x**y,m,i)])for i in l]
# l=[[3,1,0],[0,3,0],[1,1,1],[5,0,0],[2,2,0],[3,0,1],[0,2,1],[4,1,0]]
# m=[2,3,5]
# print(pf(m,l))
l=[[1,3,2],[3,1,4],[3,5,4],[5,2,3],[5,4,3],[7,1,4],[7,5,4],[9,3,2]]
t=[[''for i in[1]*9]for _ in[1]*5]
for k in l:t[k[1]-1][k[0]-1]=k[2]
[*map(print,t)]