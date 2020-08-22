from kategori import Kategori
from rett import Rett

class Meny:

    # katNavn = ["frokost", "middag", "kveldsmat"]
    def __init__(self, katNavn):
        self._meny = {}

        for linje in katNavn:
            self._meny[linje] = self._lesKategoriFil(linje+".txt")


    #liste = ["saus", "egg"]
    def hentRedusertMeny(self, unngaListe):
        nyMeny = {}

        for x in self._meny:
            katObjekt = self._meny[x]
            rettList = katObjekt.hentOkRetter(unngaListe)
            kat = Kategori(x, rettList)
            nyMeny[x] = kat

        return nyMeny


    #"frokost.txt / "middag.txt" / "kveldsmat.txt"
    def _lesKategoriFil(self, filnavn):
        fil = open(filnavn)
        #liste med rett-objekter
        retter = []

        #skaper rett-objekter
        for linje in fil:
            liste = []
            bit = linje.strip().split("  ")
            navn = bit[0]
            pris = bit[1]
            split = bit[2].split(", ")
            for x in split:
                liste.append(x)
            retter.append(Rett(navn, pris, liste))

        fil.close()
        #returner kategori-objekter
        kategori = Kategori(filnavn[:-4], retter)
        return kategori

