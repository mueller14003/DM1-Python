gcd = lambda a,b: a if b==0 else not a%b and b or gcd(b,a%b)
is_coprime = lambda x,y: gcd(x,y)==1

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)

def rsa_encrypt(message,n,e,encoder=None):
    encoded_message = (encoder or (lambda x: x))(message)
    return [pow(encoded_message[x],e,n) for x in range(len(encoded_message))]

def rsa_decrypt(encrypted,n,d,decoder=None):
    decrypted = [pow(encrypted[x],d,n) for x in range(len(encrypted))]
    return (decoder or (lambda x: x))(decrypted)

def round_trip(message,n,e,d,encoder=None,decoder=None):
    return rsa_decrypt(rsa_encrypt(message,n,e,encoder),n,d,decoder)

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

eng_to_dec = lambda n: [alphadec(i) for i in n]

dec_to_eng = lambda n: [decalpha(i) for i in n]

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

def get_rsa_vals(p,q):
    n,tee,e,d=p*q,(p-1)*(q-1),1,1
    for i in range(2,int(tee/2+1)):
        if is_coprime(i,tee): e=i
    d = egcd(e,tee)[1]
    return (n,e,d)

def test_rsa(message,p,q):
    n,e,d = get_rsa_vals(p,q)
    encrypted = rsa_encrypt(message,n,e,eng_to_dec)
    decrypted = rsa_decrypt(encrypted,n,d,dec_to_eng)
    success = (message == decrypted)
    output = "{} was encoded and decrypted as {} then decrypted and decoded as {}".format(message,encrypted,decrypted)
    if success: output += " successfully (like a boss)."
    else: output += " and was a complete failure."
    print(output,"\nString Form: {}".format(list_to_string(decrypted)))

test_rsa(['i',' ','a','m',' ','a','w','e','s','o','m','e'],47,73)