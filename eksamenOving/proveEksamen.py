print("------------------------------------------------------------------------------")

#oppg 1
tall = (3+1) * 2
tall = tall - 5

print("oppg 1 - tall:", tall)
print("------------------------------------------------------------------------------")

tall = 7
tekst = "a"

if tall>10:
  tekst = tekst + "b"

elif tall<5:
  tekst = tekst + "c"

else:
  tekst = tekst + "d"

print("oppg 2 - tekst:", tekst)
print("------------------------------------------------------------------------------")

#oppg 3
a = 0

for b in [2,4,1]:
    a = 2*a + b

print("oppg 3 - for:", a)
print("------------------------------------------------------------------------------")

#oppg 4
tallene = [ ]

a = 0
b = 1

while a<4:
    tallene.append(b)
    b = b*2
    a = a+1

print("oppg 4 - while:", tallene[0] + tallene[3])
print("------------------------------------------------------------------------------")

#oppg 5
def kalkuler(tall):
    tall = tall + 1
    return tall * 2

print("oppg 5 - kalkulator:", kalkuler(2) + kalkuler(4))
print("------------------------------------------------------------------------------")

#oppg 6
class Tall:

    def __init__(self, a):
        self._a = a

    def m1(self, c):
        self._a = self._a + c

    def m2(self):
        self._a = self._a * 2

    def m3(self):
        return self._a + 10


t1 = Tall(5)
t2 = Tall(2)
t1.m2()
t2.m1(t1.m3())

print("oppg 6 - tall:", t2.m3())
print("------------------------------------------------------------------------------")

#oppg 7
class Person:

    def __init__(self, navn, alder):
        self._navn = navn

        self._alder = alder

    def bursdag(self):
        self._alder += 1

    def hentAlder(self):
        return self._alder

    def settAlder(self, nyAlder):
        self._alder = nyAlder

far = Person("Gjert", 48)
trener = far
trener.bursdag()

print("oppg 7 - klasse:", far.hentAlder())
print("------------------------------------------------------------------------------")

#oppg 8
far = Person("Gjert", 48)
trener = far
trener.settAlder(60)

print("oppg 8 - alder:", far.hentAlder() )
print("------------------------------------------------------------------------------")

#oppg 9
far = Person("Gjert", 48)
trener = far
trener.bursdag()
trener = Person("Tone", 60)

print("oppg 9 - alder:", far.hentAlder() )
print("------------------------------------------------------------------------------")

#oppgave 10
def feiring(p):
    p.bursdag()

far = Person("Gjert", 48)
feiring(far)

print("oppg 10 - alder:", far.hentAlder())
print("------------------------------------------------------------------------------")

#oppgave 11
def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag

    if hjemmemaal == bortemaal:
        return "uavgjort"

    elif bortemaal > hjemmemaal:
        return bortelag

print("oppg 11 - vinnerlag:", vinnerlag("Brann", "Molde", 2, 3),"og", vinnerlag("Brann", "Molde", 2, 2))
print("------------------------------------------------------------------------------")

def forkort_lagliste(lagliste):

    return list(set(lagliste))

print("oppg 12 - forkort:", forkort_lagliste(["Molde", "Sarpsborg", "Molde", "Brann"]))
print("------------------------------------------------------------------------------")

#oppgave 13
def legg_inn_null_maal(lagliste):
    ordbok = {}

    for x in lagliste:
        ordbok[x] = 0

    return ordbok

print("oppg 13 - null_maal:", legg_inn_null_maal(["Brann", "Molde", "Sarpsborg", "Molde", "Brann"]))
print("------------------------------------------------------------------------------")

#oppgave 14
def ekstraher_lagliste(fn):
    lagnavn = []
    fil = open(fn)

    for x in fil:
        biter = x.split(" ")
        lagnavn.append(biter[0])
        lagnavn.append(biter[1])

    fil.close()
    return lagnavn

print("oppg 14 - ekstraher:", ekstraher_lagliste("lagliste2.txt"))
print("------------------------------------------------------------------------------")

#oppgave 15
def regn_poengsum(fn):
    # tar imot liste med hjemmelag, bortelag, hjemmemaal, bortemaal
    # returnerer en liste med alle lagene
    liste = ekstraher_lagliste(fn)

    # tar imot liste med alle lagnavn
    # returnerer en mengde med alle lagene
    mengde = forkort_lagliste(liste)

    # tar imot en liste med alle lagnavn
    # returner ordbok med alle lag med 0 maal
    ordbok = legg_inn_null_maal(mengde)

    fil = open(fn)

    for x in fil:
        biter = x.split()
        hjemmelag = biter[0]
        bortelag = biter[1]
        hjemmemaal = biter[2]
        bortemaal = biter[3]
        vinner = vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal)

        if vinner == "uavgjort":
            ordbok[hjemmelag] += 1
            ordbok[bortelag] += 1

        elif vinner == hjemmelag:
            ordbok[hjemmelag] += 3

        #else:
        elif vinner == bortelag:
            ordbok[bortelag] += 3

    fil.close()
    return ordbok

print("oppg 15 - poengsum:", regn_poengsum("lagliste2.txt"))
print("------------------------------------------------------------------------------")

#oppgave 16
def gull(lagoversikt):

    storst = 0

    for x in lagoversikt:
        poeng = lagoversikt[x]

        if poeng > storst:
            storst = poeng
            vinnerlag = x

    return vinnerlag


print("oppg 16 - gull:", gull({"Brann":2, "Molde":3, "Sarpsborg":1}))
print("------------------------------------------------------------------------------")

#oppgave 17
def finn_gull(fn):
    print("Navn paa vinnerlag:", gull(regn_poengsum(fn)))

finn_gull("lagliste2.txt")
print("------------------------------------------------------------------------------")

#oppgave 25
def godkjenn(alder):
    fam1 = alder[0]
    fam2 = alder[1]
    antallMyndigFam1 = []
    antallMyndigFam2 = []

    for x in fam1:
        if x >= 18:
            antallMyndigFam1.append(x)

    for y in fam2:
        if y >= 18:
            antallMyndigFam2.append(y)

    if len(antallMyndigFam1) >= 1 and len(antallMyndigFam2) >= 1:
        return True
    else:
        return False

print("oppg 25 T1 - myndigperson (har begge familie myndig person?):", godkjenn([[10,2,30],[20,1]]))
print("oppg 25 T2 - myndigperson (har begge familie myndig person?):", godkjenn([[10,2,30],[10,1]]))
print("------------------------------------------------------------------------------")
