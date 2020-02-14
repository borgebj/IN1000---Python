
liste = [10, 2, 4, 6, 3, 9, 5]

storst = liste[0]

for x in liste:
    if x > storst:
        storst = x
print(storst)

minste = liste[0]

for x in liste:
    if x < minste:
        minste = x
print(minste)