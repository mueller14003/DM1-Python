# a=[0,1]
# for _ in[1]*29:a+=[sum(a[-2:])]
# [*map(print,a)]

# Winner
#a=[0,1];exec('print(a[-2]);a+=[sum(a[-2:])];'*31)

# a,b=0,1
# for i in[1]*29:
#  c=a+b
#  print(c)
#  a=b
#  b=c

# f=lambda n:n if n<2else f(n-1)+f(n-2)
# [print(f(i))for i in range(31)]
#s='s={0!r};print(s.format(s))';print(s.format(s))

#is_odd=lambda n:n%2
#is_even=lambda n:n%2<1

# Did this just for fun, no golf challenge
#print(['even','odd'][int(input())%2])

# PI, but with a different library - unusable for golf
# from mpmath import*;mp.dps=1001;print(pi)

