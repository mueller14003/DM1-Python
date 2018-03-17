def CMM(m, n=20):
    for i in range(0, int(m)):
        line = []
        for j in range(int(-n), int(n)+1):
            line.append(j*m+i)
        print("{}".format(line))

CMM(11, 5)

