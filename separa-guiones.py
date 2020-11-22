word = input()
delimiter = int(input())
if(delimiter <= 0):
    print("Error")
else:
    counter = 0
    newWord = ""
    for i in range(len(word)):
        counter+=1
        newWord += word[i]
        if(counter==delimiter and i<len(word)-1):
            newWord += "-"
            counter = 0
    print(newWord)