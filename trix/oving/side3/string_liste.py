
liste = ["Hei", "verden", "som", "er", "stor"]

for x in range(len(liste)):
    print(liste[x])

string = input("Skriv tekst: ")

liste.append(string)
print(liste)
for y in range(len(liste)):
    print(liste[y])