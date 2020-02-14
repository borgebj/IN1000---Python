# coding=utf-8
"""Program som bruker funksjoner og kommandoen (count) til å beregne verdier og telle antall bokstaver i et ord"""

#for å få bedre oversikt i terminalen.
print("---------------------------------------------------------\n")

#funksjon som har to heltall som parametre og som legger sammen disse to.
def adder(a, b):
    return a + b

#kaller opp funksjonen 2 ganger med ulike heltall i hver.
sum = adder(5,20)
sum2 = adder(66,44)

#printer ut resultatet av de 2 funksjonene.
print("Første sum er:", "[", sum, "]")
print("Andre sum er:", "[", sum2, "]")

#skiller 1 og 2/3
print("")

#ber bruker om tekststreng og bokstav i to ulike variabler.

#funksjon som tar minTekst og teller hvor mange ganger minBokstav er i minTekst ved hjelp av count)
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

#2 variabler definert av bruker.
minTekst = input("Skriv en setning: ")
minBokstav = input("Skriv en bokstav du ønsker å sjekke: ")

#endret i deloppgave 3, variabelen lengde blir definert som resultatet av funksjonen "tellForekomst", hvor brukeren selv velger mintekst og minBokstav.
lengde = tellForekomst(minTekst, minBokstav)
#om bokstaven kommer flere enn 1 ganger, printes ut teksten med "# ganger i ordet"
if lengde > 1:
    # skriver ut bokstaven ↓, hvor mange ganger bokstaven er i ordet, ↓ og teksten skrevet fra brukeren ↓.
    print("Bokstaven", minBokstav, "kommer", tellForekomst(minTekst, minBokstav), "ganger i ordet", minTekst+(".\n"))
#ellers printes ut teksten med "# gang i ordet"
else:
    print("Bokstaven", minBokstav, "kommer", tellForekomst(minTekst, minBokstav), "gang i ordet", minTekst + (".\n"))

print("---------------------------------------------------------")
