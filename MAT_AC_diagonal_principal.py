def diagonal(matriz):
    resultado = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                resultado.append(matriz[i][j])
    return resultado
    
matriz = []
nfilas = int(input())
ncolumnas = int(input())
fila = list()
if nfilas != ncolumnas:
    print("la matriz no es cuadrada")
else:
    for i in range(nfilas):
        for j in range(ncolumnas):
            fila.append(int(input()))
        matriz.append(fila.copy())
        fila.clear()
    print(diagonal(matriz))
         
            