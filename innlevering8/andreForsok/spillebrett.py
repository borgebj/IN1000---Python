from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._genNr = 0
        self._antallLevende = 0
        self._rutenett = []

        for x in range(rader):
            liste = []
            self._rutenett.append(liste)
            for y in range(kolonner):
                celle = Celle()
                liste.append(celle)

        self._generer()

    def _generer(self):
        for liste in self._rutenett:
            for celle in liste:
                if randint(0, 2) == 0:
                    celle.settLevende()

    def tegnBrett(self):
        print("\n"*50)
        for a in range(self._kolonner): print("───", end="")
        for liste in self._rutenett:
            print()
            for celle in liste:
                print(celle.hentStatusTegn(), end="  ")
        print()
        for a in range(self._kolonner): print("───", end="")


    def oppdatering(self):
        self._genNr += 1
        self._antallLevende = 0
        print("\nGenerasjon:     ", self._genNr)
        print("Antall levende: ", self.finnAntallLevende())
        for a in range(self._kolonner): print("───", end="")
        print()

        skalDo = []
        skalLeve = []

        for x in range(self._rader):
            for y in range(self._kolonner):

                # henter antall naboer
                naboer = self.finnNabo(x, y)
                antall = self.hentLevende(naboer)
                celle = self._rutenett[x][y]

                # deretter: sjekk antall levende naboer
                if celle.erLevende():
                    if antall < 2 or antall > 3:
                        skalDo.append(celle)
                else:
                    if antall == 3:
                        skalLeve.append(celle)

        # selve oppdateringen
        for a in skalLeve:
            a.settLevende()
        for b in skalDo:
            b.settDoed()

    # egen metode
    def hentLevende(self, naboer):
        levende = 0
        for celle in naboer:
            if celle.erLevende():
                levende += 1
        return levende

    def finnAntallLevende(self):
        for liste in self._rutenett:
            for celle in liste:
                if celle.erLevende():
                    self._antallLevende+=1
        return self._antallLevende


    def finnNabo(self, rad, kol):
        naboer = []
        for i in range(-1, 2):  # En nabo er enten på raden før, samme rad eller neste rad.
            for j in range(-1, 2):  # På samme måte som rad.
                naboRad = rad + i
                naboKol = kol + j
                gyldig = True

                if naboRad == rad and naboKol == kol:
                    gyldig = False

                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False

                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False

                if gyldig:
                    naboer.append(self._rutenett[naboRad][naboKol])
        return naboer


