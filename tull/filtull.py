from random import randint

minFil = open("bs.txt", "a")

inp1 = input("\nSkriv inn navn på rommet: ")
inp2 = input("Skriv inn etasje på rommet: ")
print("")

rom = (inp1, inp2)
rom = str(rom)

minFil.write(rom)

minFil = open("bs.txt", "r")

for x in minFil:
    print(x)

minFil.strip()