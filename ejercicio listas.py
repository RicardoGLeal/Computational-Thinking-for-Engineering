lista = [-5,77,[2,4,6,8,[10,20,30]], "!no puedo!"]
lista[-1] = "si pude!"
print(lista)
lista[2][0] = 777
print(lista[2][-1])
print(lista[-2:])
lista[0] = ["no","si"]
print(lista[0:-1:2])
lista[0::2] = [0,0]
print(lista)                   
    