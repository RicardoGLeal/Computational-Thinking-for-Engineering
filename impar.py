def checkIfDecimal(n):
    decimal = n%1
    decimal = (-decimal)//1
    decimal = int(-decimal)
    return decimal

def redondeo_impar(n):
    decimal = checkIfDecimal(n)
    n = n//1
    impar = -(n%2)
    impar += 1
    x = round(decimal)
    n = n + (impar * x)
    return int(n)


x = float(input())
print(redondeo_impar(x))