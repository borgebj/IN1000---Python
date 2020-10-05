print("---------------------------------\n")

# returner antall bokstaver i param1
def hentBokstaver(ord):
    antall = 0
    for bokstav in ord: antall += 1
    return antall

def hentOrdbok(setning):
    ordbok = {}
    for hvert in setning.split():
        ordbok[hvert] = setning.count(hvert)
    return ordbok


setning = input("Skriv en setning\n> ")
ordbok = hentOrdbok(setning)

print("\n\nDet er", len(ordbok), " unike ord i og ", len(setning.split()), "totale ord i setningen din ")
for nokkel in ordbok:
    print("Ordet ["+nokkel+"] forekommer", ordbok[nokkel], "antall ganger, og har", hentBokstaver(nokkel), "bokstaver")

print("\n---------------------------------")
