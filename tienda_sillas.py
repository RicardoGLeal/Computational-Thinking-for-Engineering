def calcular_costo(tipo_silla, num_sillas):
    if(tipo_silla == 'B'):
        return 700 * num_sillas
    elif(tipo_silla == 'E'):
        return 900 * num_sillas
    elif(tipo_silla == 'L'):
        return 1500 * num_sillas
        
def calcular_descuento(subtotal, cliente):
    if(cliente == 'N'):
        if(subtotal >= 10000 and subtotal < 20000):
            return int(subtotal*0.10)
        elif(subtotal >= 20000):
            return int(subtotal*0.15)
        else:
            return 0
    elif(cliente == 'F'):
        return int(subtotal*0.20)
    else:
        return 0

tipo_silla = input()
cliente = input()
num_sillas = int(input())

costo = calcular_costo(tipo_silla, num_sillas)
descuento = calcular_descuento(costo, cliente)

print(costo)
print(descuento)
print(costo-descuento)
