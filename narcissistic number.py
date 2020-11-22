def solve(n):
    num = n
    suma = 0
    while num > 0:
        dig = num%10 
        suma = suma + len(n)
        num = num//10
    if(suma == n):
        return True
    else:
        return False
    
print(solve(153)) 