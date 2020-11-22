def convertir(h, m, s):
    s = s + (m*60) + (h*3600)
    return s
     
h = int(input("horas: "))
m = int(input("minutos: "))
s = int(input("segundos: "))

print(convertir(h, m, s))