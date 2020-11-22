def primos(n,m):
    for i in range(n,m+1):
        if((i%2 == 0 and i!=2) or (i%3 == 0 and i!=3) or (i%5 == 0 and i!=5) or (i%7 == 0 and i!=7) or i==1):
            print(i)
        

n = int(input())
m = int(input())

primos(n,m)