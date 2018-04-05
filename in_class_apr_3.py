# t=lambda x:sum([(-1)**n*x**(2*n-1)/(2*n-1)for n in range(1,10000)])
# p=4*(4*t(1/5)-t(1/239))
# print(p)

# def p():
#     q=t=k=1
#     m=x=3
#     r=0
#     for j in range(4320):
#         if 4*q+r-t<m*t:
#             yield m
#             q,r,t,k,m,x=10*q,10*(r-m*t),t,k,(10*(3*q+r))//t-10*m,x
#         else:q,r,t,k,m,x=q*k,(2*q+r)*x,t*x,k+1,(q*(7*k+2)+r*x)//(t*x),x+2
# print("".join(['3.']+[str(i)for i in p()][1:]))

def p(z=10,r=0):
 q=t=k=1
 m=x=3
 for j in range(4320):
  if 4*q+r-t<m*t:
   yield m
   q,r,m=z*q,z*(r-m*t),z*(3*q+r)//t-z*m
  else:q,r,t,k,m,x=q*k,(2*q+r)*x,t*x,k+1,(q*(7*k+2)+r*x)//(t*x),x+2
print('3.'+''.join([*map(str,p())][1:]))