def primo(num):
    if(num>1):  
        for i in range (2, num+1):
            if(num%i == 0):
                if(i==num):
                    return i
                else:
                    return False
        return False
    elif (num==1):
        return False
    else:
        for i in range (num+1, 0):
            if(num%i == 0):
                    return i
        return False
        
    

num = int(input())
print(primo(num))