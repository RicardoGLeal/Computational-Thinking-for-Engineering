
entered = "[[3, 1], [3, -8], [7, 5]]"
matriz = StringToMatriz(entered)

def StringToMatrix(matriz)::
    matriz = matriz.replace("[","")
    matriz = matriz.replace("]]","")
    matriz = matriz.replace(" ","")
    x = matriz.split("],")
    for fila in x:
        datos = fila.split(",")
        lista = []
        for dato in datos:
            lista.append(int(dato))
        return(matriz)
