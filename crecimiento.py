import math

poblacion = int(input())
tiempo = int(input())
tasa = float(input())

res = math.floor(poblacion*(math.exp(tasa*tiempo)))
print(res)
