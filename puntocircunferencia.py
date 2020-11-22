import math
def comprobar_punto(x1,y1,x2,y2,radio):
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if(dist > radio):
        return "FUERA"
    elif(dist == radio):
        return "SOBRE"
    else:
        return "DENTRO"
    
radio = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(comprobar_punto(x1,y1,x2,y2,radio))