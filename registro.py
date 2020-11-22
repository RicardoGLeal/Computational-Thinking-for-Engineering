registro = {}
while(True):
    word = input()
    if(word != "---"):
        key = word[0]
        if key in registro:
            registro[key].append(word)
        else:
            registro[key] = [word]
    else:
        break

consultas = []
while(True):
    cons = input()
    if(cons != "***"):
        consultas.append(cons)
    else:
        break
for i in consultas:
    if i in registro:
        print(registro[i])
    else:
        print("No existen palabras que inicien con esa letra en el registro.")
print("Las consultas finalizaron")