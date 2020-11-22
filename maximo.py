def calcular_mayor(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>c):
        return b
    else:
        return c
        

a = int(input())
b = int(input())
c = int(input())
print(calcular_mayor(a,b,c))
