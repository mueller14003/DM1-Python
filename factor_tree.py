is_prime = lambda n: False if False in [n%i != 0 for i in range(2,int(n**.5)+1)] else True

class Tree(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

    def pre_print(self):
        if not self.left and not self.right:
            return "{}".format(None)
        if not self.left and not isinstance(self.right, Tree):
            return "{}".format(self.right)
        if not self.right and not isinstance(self.left, Tree):
            return "{}".format(self.left)
        if not isinstance(self.left,Tree) and not isinstance(self.right,Tree):
            return "{} . {}".format(self.left,self.right)
        if isinstance(self.left,Tree) and not isinstance(self.right,Tree):
            return "({}) {}".format(self.left.pre_print(),self.right)
        if isinstance(self.right,Tree) and not isinstance(self.left,Tree):
            return "({}) {}".format(self.left,self.right.pre_print())
        if isinstance(self.left,Tree) and isinstance(self.right,Tree):
            return "({}) {}".format(self.left.pre_print(),self.right.pre_print())

    def tree_out(self):
        print("({})".format(self.pre_print()))

def reverse_gcd(n):
    a,b = 1,1
    for i in range(2,n//2+1):
        if i * (n//i) == n:
            a,b = n//i,i
            if a**.5 == int(a**.5) and b**.5 == int(b**.5):
                if (a**.5)**.5 == int((a**.5)**.5) and (b**.5)**.5 == int((b**.5)**.5):
                    return (a,b)
    return (a,b)

def make_factor_tree(n):
    if is_prime(n):
        return Tree(1,n)
    if is_prime(reverse_gcd(n)[0]) and is_prime(reverse_gcd(n)[1]):
        return Tree(reverse_gcd(n)[0],reverse_gcd(n)[1])
    if is_prime(reverse_gcd(n)[0]):
        return Tree(reverse_gcd(n)[0],make_factor_tree(reverse_gcd(n)[1]))
    if is_prime(reverse_gcd(n)[1]):
        return Tree(make_factor_tree(reverse_gcd(n)[0]),reverse_gcd(n)[1])
    else:
        return Tree(make_factor_tree(reverse_gcd(n)[0]),make_factor_tree(reverse_gcd(n)[1]))

make_factor_tree(1296).tree_out()


