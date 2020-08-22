
dict = {"melk":14.90, "brod":24.90, "yoghurt":12.9, "pizza":39.9}

print("")
print(dict)

vare = input("\nNy vare: ").lower()
totalLagt = 0
total = 0

while vare != "":
    pris = float(input("Pris pa tilsvarende vare: "))
    dict[vare] = pris
    totalLagt += pris
    vare = input("\nNy vare: ").lower()
for x in dict:
    total += dict[x]

print("")
print(dict)
print("")
print("Total på alle varer:", total)
print("Total på alle lagt til:", totalLagt)
print("")