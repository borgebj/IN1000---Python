import time
# coding=utf-8
"""Program som inneholder funksjoner for både addisjon, subtraksjon, divisjon og konvertering fra tommer til centimeter. Programmet tar inn input fra bruker, og regner dette VHA funksjonene."""

print("")

#funksjon som adderer verdi x med y
def addisjon(x, y):
    addSum = x + y
    print("Resultat av addering:", addSum)
    return addSum

time.sleep(0.5)

#assertion for addisjon funksjonen, med positive og negative tall.
print("Assertion for funksjon 1")
assert addisjon(3, 3) == 6
assert addisjon(-3, 3) == 0
assert addisjon(-3, -3) == -6

print("")
time.sleep(1.5)

#funksjon som subtraherer verdi a med b
def subtraksjon(a, b):
    subSum = a - b
    print("Resultat av subtraksjon:", subSum)
    return subSum

#assertion for subtraksjon funksjonen, med positive og negative tall.
print("Assertion for funksjon 2")
assert subtraksjon(3, 3) == 0
assert subtraksjon(-3, 3) == -6
assert subtraksjon(-3, -3) == 0

print("")
time.sleep(1.5)

#funksjon som dividerer verdi t med s
def divisjon(t, s):
    divSum = t / s
    print("Resultat av divisjon:", divSum)
    return divSum

#assertion for divisjon funksjonen, med positive og negative tall.
print("Assertion for funksjon 3")
assert divisjon(3, 3) == 1
assert divisjon(-3, 3) == -1
assert divisjon(-3, -3) == 1

print("")
time.sleep(1.5)

#funksjon som regner fra tommer til centimeter ved hjelp av en parameter som brukeren velger.
def tommerTilCm(antallTommer):
    #Sjekker om antallTommer er over 0
    assert antallTommer > 0
    cm = antallTommer * 2.54
    print("\nKonvertering fra tommer til centimeter:")
    print("Resultat av konvertering:", cm)
    return cm

time.sleep(1.5)
#tester addisjon funksjonen ved å legge sammen 2 egendefinerte verdier. oppg 1.1
addisjon(6, 3)

time.sleep(1.5)
# tester tommerTilCm funksjonen ved å angi antallTommer = 28. oppg 1.3
tommerTilCm(28)


#funksjon som har 2 parametre som henter input fra bruker, og bruker dette for å kalle opp resten av funksjonene med input som parametre.
def skrivBeregninger():
    print("\nUtregninger:")
    # 2 inputs fra bruker som blir gjort om til flytall.
    inp1 = input("Skriv inn tall 1: ")
    inp1 = float(inp1)
    inp2 = input("Skriv inn tall 2: ")
    inp2 = float(inp2)
    print("")

    #de 3 første funksjonene med input som parametre.
    addisjon(inp1, inp2)
    subtraksjon(inp1, inp2)
    divisjon(inp1, inp2)

    time.sleep(1.5)

    # input for konvertering fra tommer til cm (gjøres også om til flytall).
    inp3 = input("\nSkriv inn antall tommer: ")
    inp3 = float(inp3)

    #til slutt kalles tommer til centimterer funksjonen opp med argument tatt fra input ovenfor-
    tommerTilCm(inp3)

(print(""))

time.sleep(1.5)
#prosedyren "skrivBeregninger" som inneholder alle de 4 funksjonene kalles opp.
skrivBeregninger()

print("")
