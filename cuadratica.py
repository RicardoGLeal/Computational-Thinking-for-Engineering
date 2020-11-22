import math


def ecuacion(a,b,c):
    x1 = (-b + ((b**2-(4*a*c))**0.5))/2*a
    x2 = (-b - ((b**2-(4*a*c))**0.5))/2*a
    
    
    print(x1)
    if(x1!=x2):
        print(x2)
    return

a = int(input())
b = int(input())
c = int(input())

ecuacion(a,b,c)
