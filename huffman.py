class cons(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data
        self.get_stuff = lambda n,t,c: isinstance(n,c) and n
        self.get_value = lambda n: self.get_stuff(n,data,str)
        self.get_left = lambda n: self.get_stuff(n,left,list)
        self.get_right = lambda n: self.get_stuff(n,right,list)

    def find_leaf(self,encoded,tree):
        if self.get_value(tree):
            return cons(tree,encoded)
        else:
            first,rest = encoded[0],encoded[1:]
            case = {0: self.find_leaf(rest, self.get_left(tree)), 1: self.find_leaf(rest, self.get_right(tree))}
            if first in case.keys(): return case[first]
            else: return None

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

a={'f':.1,'i':'011','s':'010','h':.08,'r':.12,'t':.15,'e':'11'}