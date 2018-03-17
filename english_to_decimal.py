def alphadec(a):
    switcher = {
        ' ': 0,
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    return switcher.get(a, "Invalid character")

def decalpha(d):
    switcher = {
        0: ' ',
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }
    return switcher.get(d, "Invalid number")

def engtodec(n):
    decimal = []
    for i in n:
        decimal.append(alphadec(i))
    return decimal

def dectoeng(d):
    english = []
    for i in d:
        english.append(decalpha(i))
    return english

def list_to_string(l):
    string = ""
    last = ""
    index = 0
    for i in l:
        if index == 0 or last == ' ':
            i = i.upper()
        string += i
        last = str(i)
        index += 1
    return string

name = ['k', 'y', 'l', 'e', ' ', 'm', 'u', 'e', 'l', 'l', 'e', 'r']

dec = engtodec(name)
print(dec)
eng = dectoeng(dec)
print(eng)
string = list_to_string(eng)
print(string)