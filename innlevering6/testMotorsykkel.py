# coding=utf-8
from motorsykkel import Motorsykkel
"""Dette programmet importerer klassen "Motorsykkel" fra motorsykkel.py. Programmet inneholder en prosedyre som kjører alt med gitte argumenter."""
#^ importerer klassen "Motorsykkel" fra filen "motorsykkel"

print("-------------------------------------------------------------------------\n")

#prosedyre som inneholder objekter som kaller opp den importerte klassen Motorsykkel
def hovedprogram():
    #3 objekter som kaller opp klassen Motorsykkel med ulike verdier
    motorsykkel = Motorsykkel("Kawasaki", "MLB84A", 151517)
    motorsykkel2 = Motorsykkel("Harley", "MDAB51", 112408)
    motorsykkel3 = Motorsykkel("BMW", "AADF63", 114958)

    #3 objekter som kaller opp metoden "skrivUt" fra klassen Motorsykkel, som da skriver ut.
    motorsykkel.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()
    print("")

    #objekt som kaller opp "kjor" fra klassen Motorsykkel, med 10 i parameter. Det vil altså øke kilometerstanden på siste objekt med 10.
    motorsykkel3.kjor(10)

    #skriver ut objekt med metoden "hentkilometerstand" fra klassen Motorsykkel.
    print("Kilometerstand etter å ha økt med 10km:", motorsykkel3.hentKilometerstand())

#kaller opp prosedyren hovedprogram som inneholder alt.
hovedprogram()

print("\n-------------------------------------------------------------------------")

