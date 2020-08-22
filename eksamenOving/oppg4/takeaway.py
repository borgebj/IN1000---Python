from meny import Meny
from kunde import Kunde

class TakeAway:

    def __init__(self, katNavn, kundefil):
        self._meny = Meny(katNavn)
        self._kundeBok = {}
        ord = self._lesKundeFil(kundefil)

        for linje in ord:

            ikkeListe = []
            split = ord[linje].split(", ")

            for x in split:
                ikkeListe.append(x)

            self._kundeBok[linje] = Kunde(linje, ikkeListe)


    def betjenKunde(self, telefonnummer):

        #oppretter kunde-objekt
        kundeObjekt = self._kundeBok[telefonnummer]

        #henter liste med string
        bestilling = kundeObjekt.velgRetter(self._meny)

        #skriver ut bestilling
        self._lagOgLeverMat(bestilling)

	#skal ikke lage fra oppgave
    def _lesKundeFil(self, kundefil):
        fil = open(kundefil)
        kundeKatalog = {}

        for linje in fil:
            linje = linje.strip().split("  ")
            tlf = linje[0]
            try:
                liste = linje[1]
            except:
                liste = " "
            kundeKatalog[tlf] = liste

        fil.close()
        return kundeKatalog

    def _lagOgLeverMat(self, bestilling):
        print("\nDu har bestillt rettene: ")
        for x in bestilling:
            print("-", x)
