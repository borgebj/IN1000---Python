print("----------[a+b]----------")

oliste  = []
for x in range(5):
    oliste.append("o")
print(oliste)

stjerneliste = []
for y in range(5):
    stjerneliste.append("*")
print(stjerneliste)

print("---------[c+d+e]-----------")

rutenett = []
rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)
print(rutenett[0])
print(rutenett[1])
print(rutenett[2])

print("-----------[f]-----------")

for a in rutenett:
    print(a)

print("-------------------------")