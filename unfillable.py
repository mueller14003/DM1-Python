def unfillable(a,b):
    unfillables = []
    for i in range(0,100):
        for j in range(0,100):
            if (a*i + b*j)%a != 0 and (a*i + b*j)%b != 0:
                unfillables.append("x: {}, y: {}, n: {}".format(i,j,(a*i + b*j)))
    print('\n'.join(unfillables))

unfillable(5,7)