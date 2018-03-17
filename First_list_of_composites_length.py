def isComposite(n):
    for d in range(2,n):
        if n%d == 0: return True
    return False

def runLength(n,l=0):
    while isComposite(n+l): l+=1
    return l

def firstRun(l,n=2):
    while runLength(n) < l: n += 1
    print(list(range(n,n+l)))

firstRun(7)
