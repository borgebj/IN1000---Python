from gave import Gave
from barn import Barn

class Julekalender:

    def __init__(self, navneliste, gavefil):
        self._gaveKalender = []

        self._lesGaveFil(gavefil)

        self._apnere = []

        for x in navneliste:
            self._apnere.append(Barn(navn))


        self._nesteApner = 0
        self._dag = 0

    def _lesGaveFil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            bit = linje.split(",")
            gaveNavn = bit[0]
            gavePris = float(bit[1])
            self._gaveKalender.append(Gave(gaveNavn, gavePris))
        fil.close()

    def nyDag(self):
        pass

    def gaveOversikt(self):
        pass


