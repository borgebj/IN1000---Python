ordbok = {}

min_fil = open("hovedsteder.csv")

for linje in min_fil:
    biter = linje.split()
    land = biter[0]
    by = biter[1]
    hovedsteder[land] = by

interesse = input("Hvilket land?: ")
hovedstad = hovedsteder[interesse]

Print("Hovedstaden er: "+ hovedstad)


