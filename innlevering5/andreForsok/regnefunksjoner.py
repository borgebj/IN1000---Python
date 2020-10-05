print("---------------------------------\n")

# oppgave 1.1
# adderer a med b og returner
def addisjon(a, b):
    return (a+b)
print("Resultat av 5 + 6 =", addisjon(5, 6))

# oppgave 1.2
# subtraherer a med b og returner
def subtraksjon(a, b):
    return (a-b)
print("Resultat av 6 - 3 =", subtraksjon(6, 3))

# deler a med b og returner
def divisjon(a, b):
    return (a/b)
print("Resultat av 10 / 5 =", subtraksjon(10, 5))

# assertion av addisjon-funksjon
assert addisjon(5, 6) == 11
assert addisjon(1, -1) == 0
assert addisjon(-5, -6) == -11

# assertion av subtraksjon-funksjon
assert subtraksjon(6, 3) == 3
assert subtraksjon(-6, 3) == -9
assert subtraksjon(-9, -9) == 0

# assertion av divisjon-funksjon
assert divisjon(10, 5) == 2
assert divisjon(10, -5) == -2
assert divisjon(-10, -5) == 2

# oppgave 1.3 - beregner tommer til cm
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer*2.54
print("5 tommer i cm =", tommerTilCm(5))

# oppgave 1.4
# tar inn input og kaller paa funksjoner ovenfor
def skrivBeregninger():
    a = int(input("\nSkriv tall a: "))
    b = int(input("Skriv tall b: "))
    print("Resultat av", a, "+", b, "=", addisjon(a, b))
    print("Resultat av", a, "-", b, "=", subtraksjon(a, b))
    print("Resultat av", a, "/", b, "=", divisjon(a, b))
    tommer = int(input("\nSkriv antall tommer: "))
    print(tommer, "antall tommer i cm =", tommerTilCm(tommer))
skrivBeregninger()

print("\n---------------------------------")