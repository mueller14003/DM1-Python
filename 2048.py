from random import randint,choice
tiles = [[0 for x in range(4)] for y in range(4)]
print(tiles)

def insert(t,o=None):
    n = 2
    l = choice(o) if o else randint(0,15)
    r = randint(0,9)
    if r == 0:
        n = 4
    t[l//4][l%4] = n
    return t

tiles = insert(tiles)
print(tiles)

def add_after_move(t):
    available_tiles = []
    for i in range(16):
        if t[i//4][i%4] == 0:
            available_tiles.append(i)
    t = insert(t,available_tiles)
    return t

def move_up(t):
    pass

def move_down(t):
    pass

def move_left(t):
    pass

def move_right(t):
    pass

def merge(t):
    pass #2 + 2 = 4