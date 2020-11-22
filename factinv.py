def factorialInverso(fact):
    x=1
    i = 0
    while(i < fact):
       i+=1
       x*=i 
       if(x==fact):
          return str(fact)+" = "+str(i)+"!"
    return "El "+str(fact)+" no corresponde a ningún número factorial." 

fact = int(input())
print(factorialInverso(fact))