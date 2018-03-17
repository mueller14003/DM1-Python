ax_by = lambda a,b,c: ["x: {}, y: {}".format(x,int((a*x-c)/b)) for x in range(-49,50) if c in [a*x + b*y for y in range(-49,50)]]
print('\n'.join(ax_by(91,11,1)))