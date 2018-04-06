a=[0,1]
for _ in[1]*29:a+=[sum(a[-2:])]
[*map(print,a)]

# a,b=0,1
# for i in[1]*29:
#  c=a+b
#  print(c)
#  a=b
#  b=c

# f=lambda n:n if n<2else f(n-1)+f(n-2)
# [print(f(i))for i in range(31)]
