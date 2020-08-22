
print("")

tall = int(input("Skriv inn tall: "))

binaer = ""
while tall != 0:
    temp = tall % 2
    tall = tall // 2
    binaer += str(temp)+" "
print("Tallet er", binaer,"i binaert")

print("")