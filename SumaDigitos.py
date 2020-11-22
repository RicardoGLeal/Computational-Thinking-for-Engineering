def sumardigitos(lista):
    res = 0
    while((len(lista))>1):
        res = 0
        for i in range(0, len(lista)):
            res += int(lista[i])
        lista = list(str(res))
        print(res)


num = int(input())
lista = list(str(num))
sumardigitos(lista)

