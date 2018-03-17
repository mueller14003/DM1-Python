def find_x_and_y(a,b):
    work = []
    for i in range(-49,50):
        for j in range(-49,50):
            if a*i + b*j == 1:
                work.append("x: {}, y: {}".format(i,j))
    print('\n'.join(work))

find_x_and_y(91,11)