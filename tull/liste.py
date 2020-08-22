
tall1 = [1, 2, 3, 4, 5]

tall2 = [5, 4, 2, 3, 1]
liste = []
nyListe = []

if len(tall1) == len(tall2):
    lengde = len(tall1)
elif len(tall1) > len(tall2):
    lengde = len(tall1)
else:
    lengde = len(tall2)

for x in range(lengde):
    nyListe.append(tall1[x] + tall2[x])


print(tall1)
print(tall2)
print(" |  |  |  |  |")
print(nyListe)