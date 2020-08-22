
personer = {}

inp = input("\nOnsker du a fortsette?: ")

print("")
while inp.lower() == "y":
    navn = input("Skriv inn navn: ").lower()
    alder = int(input("Skriv inn alder: "))
    if alder < 0 or alder > 150:
        alder = int(input("Skriv inn alder: "))

    personer[navn] = alder

    inp = input("\nOnsker du a fortsette?: ")
    print("")

print("")

bokstav = input("Skriv inn en bokstav: ")
while len(bokstav) != 1:
    bokstav = input("Skriv inn en bokstav: ")

if len(personer) == 0:
    print("\nListen er tom")
else:
    for x in personer:
        if bokstav.lower() == x[0]:
            print("\nNavn:",x," Alder:",personer[x])
        else:
            print("\nDet er ingen med",x, "som forbokstav")

print("")