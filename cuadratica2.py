import math


def ecuacion(a,b,c):
    x1 = (-b + ((b**2-(4*a*c))**0.5))/2*a
    x2 = (-b - ((b**2-(4*a*c))**0.5))/2*a
    
    if(x1.imag != 0):
        if(x1.imag > 0):
            #solucion1 = (round(x1.real),"+",x1.imag)
            print(str((round(x1.real,1)))+" + "+str(x1.imag)+"i")
        else:
            print(str((round(x1.real,1)))+" - "+str(x1.imag*-1)+"i")
    else:
        print(x1)

    if(x1!=x2):
        if(x2.imag != 0):
            if(x2.imag > 0):
            #solucion1 = (round(x1.real),"+",x1.imag)
                print(str((round(x1.real,1)))+" + "+str(x2.imag)+"i")
            else:
                print(str((round(x1.real,1)))+" - "+str(x2.imag*-1)+"i")
        else:
            print(x2)

a = int(input())
b = int(input())
c = int(input())
ecuacion(a,b,c)

