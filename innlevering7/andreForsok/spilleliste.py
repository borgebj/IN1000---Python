from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            setning = linje.strip().split(";")
            self._sanger.append(Sang(setning[1], setning[0]))
        fil.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        utvalg = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                utvalg.append(sang)
        return utvalg