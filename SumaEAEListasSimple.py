
def solicitarLista():
    x=0
    i=0
    list1 = list()
    while (x != '/'):
        x = input()
        if(not(x=='/')):
            list1.append(int(x))
        else:
            return list1
    return list1

def sumarListas(lista1, lista2):
    lista3 = list()
    for i in range (len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    return lista3
        
lista1 = solicitarLista()
lista2 = solicitarLista()


if(input()=='*'):
    print(sumarListas(lista1,lista2))
