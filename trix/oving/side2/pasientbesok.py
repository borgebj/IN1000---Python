
pasientbok = [[4, 6],
              [3, 4, 5],
              [21, 22, 29]]

def maxBesok():
    pasientnr = 0

    for x in range(len(pasientbok)):
        if len(pasientbok[x]) > len(pasientbok[0]):
            pasientnr = x

    return pasientnr + 1


def farrestBesok():
    pasientnr = 0

    for x in range(len(pasientbok)):
        if len(pasientbok[x]) < len(pasientbok[0]):
            pasientnr = x

    return pasientnr + 1

def alleBesok():
    totalBesok = 0

    for x in pasientbok:
        totalBesok += len(x)
    return totalBesok

def hvemVarPaaDato():
    inp = int(input("Skriv inn dato: "))
    if 1 > inp or 31 < inp:
        print("Ugyldig dato")
    else:
        var = []
        for x in range(len(pasientbok)):
            if inp in pasientbok[x]:
                var.append(x+1)
        if not var:
            return "ingen"
        return var



print("\nPasient nr",maxBesok(),"har mest besok")
print("Pasient nr", farrestBesok(),"har farrest besok")
print("Antall totalbesok:",alleBesok(),"\n")
print("Pasient nr den gitte dagen:", hvemVarPaaDato(),"\n")





