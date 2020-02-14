"""klasse fil som først henter tittel og artist fra bruker gjennom kall av objekt, og som inneholder ulike metoder"""
# coding=utf-8
class Sang:

    #konstruktør med 2 instansvariabler som blir opprettet
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    #metode som printer ut den valgte sangen og artisten
    def spill(self):
        print("Spiller nå:", self._tittel, "av", self._artist)

    #metode som sjekker om argumentet "navn" finnes i instansvariabelen "Artist"
    def sjekkArtist(self, navn):
        #parameter blir splittet til en liste
        navnSplit = navn.split()

        #for hvert ord i listen:
        for x in navnSplit:
            #om ordet finnes i instansvariabelen "artist", returner True
            if x in self._artist:
                return True
        #ellers return False
        return False

    #metode som har parameter "tittel"
    def sjekkTittel(self, tittel):
        #om tittel (i små bokstaver) er det samme som instansvariabelen tittel (i små bokstaver)
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

    #metode som har parameterne artist og tittel
    def sjekkArtistogTittel(self, artist, tittel):
        #samme som i sjekkArtist: splitter artist-argumentet, og sjekker med for-løkke for hvert element
        artist = artist.split()
        for x in artist:
            #for hvert element i listen, gjør en if sjekk som ser om argument-tittelen er lik instansvariabelen tittel
            if x in self._artist:
                if tittel.lower() == self._tittel.lower():
                    #om både et eller flere element finnes i instansvariabelen artist og argument-tittelen er lik instansvariabelen tittel, returnerer programmet True
                    return True
        #ellers returnerer false
        return False