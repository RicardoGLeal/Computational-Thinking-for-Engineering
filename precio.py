bulto = int(input())
precio = float(input())
subtotal = bulto * precio
impuestos = subtotal * 0.16
total = subtotal + impuestos
print(subtotal)
print(impuestos)
print(total)