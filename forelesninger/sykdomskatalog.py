from sykdom import Sykdom

class SykdomsKatalog:

    def __init__(self, filnavn):
        self._sykdommer = {}
        self._les_fil(filnavn)

    def sjekk_mutasjon(posisjon):
        for sykdoms_navn in self._sykdommer:
            sykdom = self._sykdommer[sykdoms_navn]
            if sykdom.er_assosiert(posisjon):
                return sykdom.hent_navn()

    def _les_fil(filnavn):
        for linje in open(filnavn):
            biter = linje.split(",")
            posisjon = int(biter[0])
            sykdoms_navn = biter[1]

            if not sykdoms_navn in self._sykdommer:
                self._sykdommer[sykdoms_navn] = Sykdom(sykdoms_navn)

            sykdom = self._sykdommer[sykdoms_navn]
            sykdom.legg_til_posisjon()
