
class Sang:
    def __init__(self, artist, tittel):
        self._tittel = tittel
        self._artist = artist

    def spill(self):
        print("Spiller '"+self._tittel+"' av artisten", self._artist)

    def hentArtist(self):
        return self._artist

    def sjekkArtist(self, navn):
        navnListe = navn.split()
        artistListe = self._artist.split()

        for x in navnListe:
            for y in artistListe:
                if x == y:
                    return True
        return False

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
        else: return False

    def __str__(self):
        return "'" + self._tittel + "' av "+self._artist