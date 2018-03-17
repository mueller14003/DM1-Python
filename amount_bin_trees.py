fact = lambda n: n*fact(n-1) if n > 1 else n
choose = lambda n,k: fact(n)/(fact(k)*fact(n-k))
bin_s_trees = lambda n: int(choose(2*n,n)/(n+1))
print(bin_s_trees(4))
