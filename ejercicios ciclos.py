import math
#Función que calcula la suma de los números pares del 2 al n

def sumapares(n):
    x=0
    for i in range(2,n+1,2):
        x+= i
    return x






def factorial(n):
    x = 1
    for i in range (n,1,-1):
        x*= i
    return x
        
        
        
        
        
        
def sumatoria(n):
    x = 0
    for i in range (1,n+1):
        if(i%2==0):
         x+= (i*i)
        else:
         x+= math.sqrt(i)
    return x

def fibonacci(n):
    x=0
    for i in range (n,0,-1):
        for j in range (0,n):
            x+=j
    return x

        
    

#x = sumapares(10)
#x = sumatoria(4)
x = factorial(6)
print(x)

#Función que calcula el factorial de n!
