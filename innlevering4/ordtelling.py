import time
# coding=utf-8
"""Dette programmet bruker funksjoner med ulike parametre for å finne ut ting som hvor langt et gitt ord/setning er, antall bokstaver og hvor mange ganger det forekommer, og deretter bruker disse funksjonene med setninger fra brukerten."""
#for å få bedre oversikt i terminalen.
print("----------------------------------------------------------------\n")


#funksjon 1, henter gitt ord fra parameter når den kalles opp.
def funksjon1(ord1):
    ord1 = len(ord1)
    return ord1

#funksjon 2, henter gitt setning fra parameter når den kalles opp.
def funksjon2(setning):
    split = setning.split()

    #variabel som inneholder en tom ordbok
    ordbok = {}

    #for løkke som ser gjennom split-ordboken.
    for ord2 in split:
        #variabelen "antall" = antall "ord" (hvert ord i listen split) i listen "split" (liste med unike ord)
        antall = setning.count(ord2)
        #legger til "ord" som mappe(nøkkelverdi) med "antall" som verdi(innholdsverdi)
        ordbok[ord2] = antall
    return ordbok


#variabel "inp" lagrer input fra bruker
inp = str(input("Skriv inn en setning: "))


#splitter ordene i setningen fra brukeren og legger dem i en liste.
nySplit = inp.split()

#bruker inp(input fra bruker) i de to tidligere funksjonene. Resultatet legges i to variabler.
res1 = funksjon1(inp)
res2 = funksjon2(inp)

#programmet venter i 1 sekund for å få bedre oversikt.
time.sleep(1)

print("\nDet er", len(nySplit), "ord i setningen din.")

for ord in res2:
    #hvis lengden på ordet er lenger enn 1, printes ut ord, antall ganger og lengde med "bokstavER"
    if len(ord) > 1:
        print("[", ord, "] forekommer", res2[ord], "antall ganger og er", len(ord), "bokstaver lang.")

    #ellers printes ut med "bokstaV"
    else:
        print("[", ord, "] forekommer", res2[ord], "antall ganger og er", len(ord), "bokstav lang.")


print("\n----------------------------------------------------------------")
