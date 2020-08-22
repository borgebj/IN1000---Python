
class Hytte:

    def __init__(self, navn, senger, pris):
        self._hytteNavn = navn
        self._antallSenger = senger
        self._prisPerPers = pris

    def hentNavn(self):
        return self._hytteNavn

    def totPris(self, antall):
        total = self._prisPerPers * antall
        return total

    def sjekkPlass(self, antall):
        if self._antallSenger > antall > 0:
            return True
        return False

    def __str__(self):
        streng = "Hyttenavnet: " + self._hytteNavn + "\nAntall senger: " + str(self._antallSenger) + "\nPris per seng: "+ str(self._prisPerPers)
        return streng

    def __eq__(self, objekt):
        return self._hytteNavn == objekt.hentNavn()


hytte = Hytte("Børge", 5, 299)
print(hytte)
#Hyttenavnet: Børge
#Antall senger: 5
#Pris per seng: 299

hytte2 = Hytte("Børge", 2, 240)
print(hytte == hytte2)
#True