def isiterable(n):
    try:_=[x for x in n]
    except TypeError:return 0
    if(len(n)==1and isinstance(n,str))or len(n)==0:return 0
    return 1


class elisp:
    def __init__(self):
        self.destroy_nest=lambda n:self.destroy_nest(n[0])if isiterable(n)and len(n)==1else n
        self.new_func=lambda f:self.make_new(None,f[1:-1])if self.valid(f)and f[0]=='c'and f[-1]=='r'else lambda n:n
        self.cr={'a':self.a,'d':self.d}
        self.new_f=lambda new,old:lambda*n:new(old(*n))
        self.valid=lambda l:1 and len(l[1:-1])!=0 or all(x=='a'or x=='d'for x in l[1:-1])

    def d(self,n,*a):
        n=self.destroy_nest(n)
        if a:return a
        if not isiterable(n):return n
        if len(n)==1:return n[0]
        if isiterable(n[1:])and len(n[1:])==1:return n[1:][0]
        return n[1:]

    def a(self,n,*a):
        n=self.destroy_nest(n)
        if a:return n
        if isiterable(n):return n[0]
        return n

    def call(self,f,*n):
        n=self.destroy_nest(n)
        if f[0]=='c'and f[-1]=='r':
            out=list(n)
            for i in list(f)[1:-1][::-1]:out=self.cr[i](out)
            return out

    def make_new(self,f,l):
        if len(l)==1:
            if f:return self.new_f(self.cr[l[0]],f)
            return self.cr[l[0]]
        if f:return self.make_new(self.new_f(self.cr[l[-1]],f),l[0:-1])
        return self.make_new(self.cr[l[-1]],l[0:-1])


print(elisp().call('cddr',[[1,2],[3,4],[6,5]]))
car = elisp().new_func('car')
print(car([[1,2],[3,4],[6,5]]))

