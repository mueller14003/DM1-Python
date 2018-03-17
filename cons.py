class cons(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

    def pre_print(self):
        if not self.left and not self.right:
            return "{}".format(None)
        if not self.left and not isinstance(self.right, cons):
            return "{}".format(self.right)
        if not self.right and not isinstance(self.left, cons):
            return "{}".format(self.left)
        if not isinstance(self.left,cons) and not isinstance(self.right,cons):
            return "{} . {}".format(self.left,self.right)
        if isinstance(self.left,cons) and not isinstance(self.right,cons):
            return "({}) {}".format(self.left.pre_print(),self.right)
        if isinstance(self.right,cons) and not isinstance(self.left,cons):
            return "({}) {}".format(self.left,self.right.pre_print())
        if isinstance(self.left,cons) and isinstance(self.right,cons):
            return "({}) {}".format(self.left.pre_print(),self.right.pre_print())

    def tree_out(self):
        print("({})".format(self.pre_print()))

cons(cons(4,5),cons(6,7)).tree_out()


# morphifyr = lambda func,l: cons(func(l[0]),morphifyr(func,l[1:])) if len(l) > 0 else None
#
# morphifyr(lambda x: x**2,[1,2,3,4]).tree_out()



# def test(a=1,b=2,c=3,d=4):
#     new_tree = cons(cons(a+b,d//b),cons(d-a,c*d))
#     new_tree.tree_out()
#
# test()
