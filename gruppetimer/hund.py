
class Hund:

    def __init__(self, kjonn, navn, alder):
        self._kjonn = kjonn
        # 1 - gutt | 0 - jente
        self._navn = navn
        self._alder = alder

    def __str__(self):
        return self._navn

    def hentHund(self):
        if self._kjonn == 0:
            return "Navn: " + self._navn + ", alder: " + str(self._alder) + ", kjonn: jente"

        return "Navn " + self._navn + ", alder: " + str(self._alder) + ", kjonn: gutt"

    def hentNavn(self):
        return self._kjonn

    def __eq__(self, annenHund):
        return self._navn == annenHund.hentNavn()