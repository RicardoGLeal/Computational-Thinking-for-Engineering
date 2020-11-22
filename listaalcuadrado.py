import math
def construirLista(num_cant):
    lista = list()
    for i in range (num_cant):
        number = int(input())
        lista.append(number)
    return lista

def elevarLista(lista):
    lista2 = list()
    for i in range(len(lista)):
        lista2.append(int(math.pow(lista[i],2)))
    return lista2
        
num_cant = int(input())
lista = construirLista(num_cant)
print(lista)
lista2 = elevarLista(lista)
print(lista2)