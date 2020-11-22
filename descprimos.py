
def buscar(num):
    while (num > 1):
        factor = descomponer(num)
        if(factor!=0):
            print(factor)
            num = int(num / factor)
        else:
            print(int(num))
            break
        
def descomponer(num):
        for i in range (2, num+1):
            if(num%i == 0):
                if(i==num):
                    return i
                else:
                    return i
        return 0


num = int(input())
buscar(num)