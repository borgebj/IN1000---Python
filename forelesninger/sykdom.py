
class Sykdom:

    def __init__(self, navn):
        self._navn = navn
        self._posisjoner = []

    def legg_til_posisjon(self, posisjon):
        self._posisjoner.append(posisjon)

    def er_assosiert(self, posisjon):
        return posisjon in self._posisjoner

    def hent_navn(self):
        return self._navn


