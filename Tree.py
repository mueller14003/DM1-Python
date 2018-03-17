class Tree(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

def pre_print(t):
    if t.left == None and t.right == None:
        return "{}".format(None)
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

root = Tree(Tree(Tree("a","b"),Tree("c","d")),Tree(Tree("e","f"),Tree("g","h")))
root2 = Tree(Tree("a","b"),Tree("c","d"))
tree_out(root)
tree_out(root2)