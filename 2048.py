from random import *
from numpy import *


def insert(t,o=None):
    l = choice(o) if o else randint(0,15)
    t[l//4][l%4] = 4 if not randint(0,9) else 2
    return t


def add_after_move(t):
    avail_t = []
    for i in range(16):
        if t[i//4][i%4] == 0: avail_t.append(i)
    return insert(t,avail_t)


def move_up(t):
    for i in range(1,len(t)):
        for j in range(len(t[i])):
            if t[i-1][j] == 0 or t[i-1][j] == t[i][j]:
                if i > 1 and (t[i-2][j] == 0 or t[i-2][j] == t[i][j]):
                    if i > 2 and (t[i-3][j] == 0 or t[i-3][j] == t[i][j]):
                        t[i-3][j] += t[i][j]
                        t[i][j] = 0
                    t[i-2][j] += t[i][j]
                    t[i][j] = 0
                t[i-1][j] += t[i][j]
                t[i][j] = 0
    return t


def move_down(t):
    for i in range(len(t)-1)[::-1]:
        for j in range(len(t[i])):
            if t[i+1][j] == 0 or t[i+1][j] == t[i][j]:
                if i < 2 and (t[i+2][j] == 0 or t[i+2][j] == t[i][j]):
                    if i < 1 and (t[i+3][j] == 0 or t[i+3][j] == t[i][j]):
                        t[i+3][j] += t[i][j]
                        t[i][j] = 0
                    t[i+2][j] += t[i][j]
                    t[i][j] = 0
                t[i+1][j] += t[i][j]
                t[i][j] = 0
    return t


def move_left(t):
    for i in range(len(t)):
        for j in range(1,len(t[i])):
            if t[i][j-1] == 0 or t[i][j-1] == t[i][j]:
                if j > 1 and (t[i][j-2] == 0 or t[i][j-2] == t[i][j]):
                    if j > 2 and (t[i][j-3] == 0 or t[i][j-3] == t[i][j]):
                        t[i][j-3] += t[i][j]
                        t[i][j] = 0
                    t[i][j-2] += t[i][j]
                    t[i][j] = 0
                t[i][j-1] += t[i][j]
                t[i][j] = 0

    return t


def move_right(t):
    for i in range(len(t)):
        for j in range(len(t[i])-1)[::-1]:
            if t[i][j+1] == 0 or t[i][j+1] == t[i][j]:
                if j < 2 and (t[i][j+2] == 0 or t[i][j+2] == t[i][j]):
                    if j < 1 and (t[i][j+3] == 0 or t[i][j+3] == t[i][j]):
                        t[i][j+3] += t[i][j]
                        t[i][j] = 0
                    t[i][j+2] += t[i][j]
                    t[i][j] = 0
                t[i][j+1] += t[i][j]
                t[i][j] = 0
    return t


def game_over(t):
    if 0 not in list(array(t).flatten()):
        for i in range(len(t)):
            for j in range(len(t[i])):
                if i == 0:
                    if t[i][j] == t[i+1][j]: return False
                    if j == 0:
                        if t[i][j] == t[i][j+1]: return False
                    if j == 3:
                        if t[i][j] == t[i][j-1]: return False
                    if t[i][j] == t[i][j-1] or t[i][j] == t[i][j+1]: return False
                if i == 3:
                    if t[i][j] == t[i - 1][j]: return False
                    if j == 0:
                        if t[i][j] == t[i][j+1]: return False
                    if j == 3:
                        if t[i][j] == t[i][j-1]: return False
                    if t[i][j] == t[i][j-1] or t[i][j] == t[i][j+1]: return False
                if t[i][j] == t[i+1][j] or t[i][j] == t[i-1][j] or t[i][j] == t[i][j+1] or t[i][j] == t[i][j-1]: return False
        return True
    return False


def restart():
    print('Move using w a s d. To quit, press q. Good luck!')
    t = insert([[0for x in range(4)]for y in range(4)])
    [print(*x)for x in t]
    return t


def console():
    t = restart()
    m = {'w': move_up, 'a': move_left, 's': move_down, 'd': move_right}
    win = 0
    again = False
    while 1:
        if game_over(t):
            g = input('Game Over? Restart? (y / n): ')
            if g == 'y':
                again = True
                break
            if g == 'n': break
            else: print('Invalid response.')
        else:
            if 2048 in list(array(t).flatten()) and win == 0:
                print('Congrats! You have reached 2048!')
                win = 1
            i = input()
            if i == 'q': break
            if i not in m.keys(): print('Not a valid entry. Please try again.')
            else:
                t = m[i](t)
                t = add_after_move(t)
                [print(*x) for x in t]

    if again:
        console()


def main():
    console()
    print('Thanks for playing!')


if __name__ == '__main__':
    main()
