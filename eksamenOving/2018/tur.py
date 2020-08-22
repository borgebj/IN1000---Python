
class Tur:

    def __init__(self, liste, string):
        self._objektListe = liste
        self._turBeskrivelse = string

    def skrivUt(self):
        print(self._turBeskrivelse, "\n")

        for x in self._objektListe:
            print(x.hentNavn())

    def sjekkPrisPlass(self, antall, maksBelop):
