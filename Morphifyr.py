class Tree(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

def pre_print(t):
    if t.left == None and t.right == None:
        return "{}".format(None)
    if t.left == None and not isinstance(t.right,Tree):
        return "{}".format(t.right)
    if t.right == None and not isinstance(t.left,Tree):
        return "{}".format(t.left)
    if not isinstance(t.left,Tree) and not isinstance(t.right,Tree):
        return "{} . {}".format(t.left,t.right)
    if isinstance(t.left,Tree) and not isinstance(t.right,Tree):
        return "({}) {}".format(pre_print(t.left),t.right)
    if isinstance(t.right,Tree) and not isinstance(t.left,Tree):
        return "({}) {}".format(t.left,pre_print(t.right))
    if isinstance(t.left,Tree) and isinstance(t.right,Tree):
        return "({}) {}".format(pre_print(t.left),pre_print(t.right))

def tree_out(t):
    print("({})".format(pre_print(t)))

def morphifyr(func,l):
    if len(l) == 0:
        return None
    return Tree(func(l[0]),morphifyr(func,l[1:]))

tree_out(morphifyr(lambda x: x**2,[1,2,3,4]))