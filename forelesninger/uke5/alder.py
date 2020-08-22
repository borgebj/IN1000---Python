ordbok = {}

fil = open("alder.csv")
maks = 0
eldstenavn = "ingen"

for x in fil:
    biter = x.split()
    navn = biter[0]
    alder = biter[1]
    alder = int(alder)
    if alder > maks:
        maks = alder
        eldstenavn = navn
print(eldstenavn, "på", maks, "år gammel")

