
oliste = []

for x in range(5):
    oliste.append("o")

stjerneliste = []

for y in range(5):
    stjerneliste.append("*")

rutenett = []

rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)

print(rutenett[0])
print(rutenett[1])
print(rutenett[2])
print("")
for a in rutenett:
    print(a)