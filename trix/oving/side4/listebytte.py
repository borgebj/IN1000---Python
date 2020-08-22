
liste = [10, 13, 19, 2, -2, 4, -5, 1, -9, 11, 29]
print(liste)

minst = liste[0]
for x in liste:
    if x < minst:
        minst = x
print("Minste tall er:", minst)

storst = liste[0]
for y in liste:
    if y > storst:
        storst = y
print("Storste tall er:", storst)


print(liste)