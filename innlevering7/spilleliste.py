"""Klasse fil som tar imot listenavn fra bruker, og som inneholder ulike metoder for en spilleliste"""
# coding=utf-8
from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #metode som skal ta imot en fil, lese hver linje, splitte hver linje og legge til et objekt med første og andre del av hver linje som argument i objektet.
    def lesFraFil(self, filnavn):
        fil = open(filnavn, "r")

        #for hver linje i fil:
        for x in fil:
            #linjen blit splittet og strippet, og tildelt variabelen "y"
            y = x.strip().split(";")
            sang = Sang(y[0],y[1])
            #legger objektet til i listen
            self._sanger.append(sang)
        fil.close()

    #metode som legger til sang-objekt i spillelisten. nySang parameteren tar inn objekt
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    #metode som fjerner sang fra spillelisten
    def fjernSang(self, sang):
        self._sanger.remove(sang)

    #metode som spiller sangen som blir oppgitt gjennom parameteren
    def spillSang(self, sang):
        #kaller opp metoden "spill()" fra klassen "Sang" med objektet "sang"
        sang.spill()

    #Metode som ikke tar inn noen argumenter - spiller alle sangene i spillelisten
    def spillAlle(self):
        for x in self._sanger:
            x.spill()

    #metode som finner en sang, med sang-tittel som parameter
    def finnSang(self, tittel):
        #for hver sang i spillelisten (self._sanger)
        for x in self._sanger:
            #variabel "y" blir tilordnet metoden "sjekkTittel" fra klassen "Sang" med "tittel" som argument.
            y = x.sjekkTittel(tittel)
            #om variabelen y returnerer "true", returneres sangen i spillelisten (x)
            if y:
                return x
        return None

    #metode som tar imot et artistnavn, sjekker om artisten er i spillelisten, og om den gjør det returnerer en liste med sangene til artisten
    def hentArtistUtvalg(self, artistnavn):
        artister = []
        for x in self._sanger:
            y = x.sjekkArtist(artistnavn)
            if y == True:
                artister.append(x)
        return artister
