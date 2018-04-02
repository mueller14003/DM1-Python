from math import *
import numpy as np

def type():
    t = input("Component or Angle (c / a)? ")
    return t

def cross():
    t = type()
    if t == "c":
        A = list(map(int, input("A: ").split()))
        B = list(map(int, input("B: ").split()))
        AxB = list(np.cross(a=A,b=B))
        BxA = list(np.cross(a=B,b=A))
        print("A x B =",AxB)
        print("B x A =",BxA)

    elif t == "a":
        A = float(input("A magnitude: "))
        B = float(input("B magnitude: "))
        theta = float(input("Angle (Degrees): "))
        AxB = A*B*sin(radians(theta))
        print("A x B =",AxB)

    else:
        print("Invalid input. Please try again:")
        cross()

cross()