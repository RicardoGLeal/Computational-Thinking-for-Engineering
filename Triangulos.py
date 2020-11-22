def comprobar_condiciones(a,b,c):
    if((a+b)>c):
        return True
    return False

def verificar_triangulo(a,b,c):
    
    if(a==b and b==c):
        return "equilatero"
    elif(a==b or a==c or b==c)
        return "isosceles"
    else
        return "escaleno"
    
    
    
    
   # if(a==b):
#         if(a==c):
#             return "equilatero"
#         else:
#             return "isosceles"
#     elif(a==c):
#         if(a==b):
#             return "equilatero"
#         else:
#             return "isosceles"
#     else:
#         return "escaleno"
#         

def main():
    x = int(input("Introduce el lado 1 "))
    y = int(input("Introduce el lado 2 "))
    z = int(input("Introduce el lado 3 "))

    if(not comprobar_condiciones(x,y,z)):
        print("Valores erroneos, prueba nuevamente")
        main()
    if(not comprobar_condiciones(x,z,y)):
        print("Valores erroneos, prueba nuevamente")
        main()
    if(not comprobar_condiciones(y,z,x)):
        print("Valores erroneos, prueba nuevamente")
        main()
        
    triangulo = verificar_triangulo(x,y,z)
    print("Tu triangulo es ",triangulo)
main()



