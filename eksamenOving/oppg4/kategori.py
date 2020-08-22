from rett import Rett

class Kategori:

    #konstruktor med 2 parametere og 2 instansvariabler
    #katNavn = "navn pa kategori" (list)
    #obListe = [liste med rett-objekter] (list)
    def __init__(self, katnNavn, obListe):
        self._katNavn = katnNavn
        self._obListe = obListe

    #metode som filtrerer liste med uonskede stoffer med rett-objekter
    #unngaListe = [en liste]  med innholdsstoff en ikke onsker (str)
    def hentOkRetter(self, unngaListe):

        rettListe = []

        for x in self._obListe:
            y = x.sjekkInnholdOK(unngaListe)
            if y == True:
                rettListe.append(x)

        return rettListe

