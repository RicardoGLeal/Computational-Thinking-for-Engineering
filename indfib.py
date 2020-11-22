
def fibonacci(value):
    fibo = list()
    fibo.append(0)
    fibo.append(1)
    for i in range(1,100):
        fibo.append(fibo[i]+fibo[i-1])
        if(fibo[i+1] == value):
            return(i+1)
    return(-1)
    
value = int(input())
print(fibonacci(value))
