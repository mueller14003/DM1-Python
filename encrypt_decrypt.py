m = [[1,1,3],[1,1,4],[1,4,3],[1,4,4],[2,1,3],[2,1,4],[2,4,3],[2,4,4]]
en = lambda m,k: [m[i]*k for i in range(0,len(m))]
en_list = lambda m,k: [en(m[i],k) for i in range(0,len(m))]
de = lambda en,dk: [en[i]%dk for i in range(0,len(en))]
de_list = lambda en,dk: [de(en[i],dk) for i in range(0,len(en))]

def test(m,k,dk):
    encrypted = en_list(m,k)
    decrypted = de_list(encrypted,dk)
    output = "{} \nwas encoded and decrypted as -\n{} \nthen decrypted and decoded as -\n{}".format(m,encrypted,decrypted)
    if decrypted == m: output += "\n- Successfully (with much swag)."
    else: output += "\n- And was a complete failure."
    print(output)

test(m,105,8)
