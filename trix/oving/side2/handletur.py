
print("\nVar meny og tilsvarende priser:")
print(f'{"":2} {"Brod":8} 20 kr')
print(f'{"":2} {"Melk":8} 15 kr')
print(f'{"":2} {"Ost":8} 40 kr')
print(f'{"":2} {"Yoghurt":8} 12 kr\n')

total = 0

brod = input("Hvor mange brod vil du kjope?: ")
total += 20*int(brod)

melk = input("Hvor mange kartonger melk vil du kjope?: ")
total += 15*int(melk)

ost = input("Hvor mange pakker ost vil du kjope?: ")
total += 40*int(ost)

yoghurt = input("Hvor mange pakker yoghurt vil du kjope?: ")
total += 12*int(yoghurt)

print("\nTotalprisen din er",total,"kroner.\n")