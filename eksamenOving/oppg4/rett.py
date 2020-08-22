
class Rett:

    def __init__(self, navn, pris, liste):
        self._navn = navn
        self._pris = pris
        self._liste = liste

    #metode som sjekker om stoff fra liste er i stoff fra konstruktor
    def sjekkInnholdOK(self, list):

        #for hvert stoff i gitt liste
        for x in list:
            #hvis stoff er i konstruktor-liste
            if x in self._liste:
                #returneres False
                return False

         #ellers er den ikke i listen, og True returneres
        return True

    #"magisk" metode som skriver ut instansvariabler som streng
    def __str__(self):
        #variabel som tar vare paa instansvariablene som skal returneres
        streng = ("- Navn: "+self._navn+
                  "\n- Pris: "+str(self._pris)+
                  " kr\n- Innhold: ")

        for x in self._liste:
            streng += x+", "
        streng += "\n"

        return streng

    #ikke i oppgaven!!
    def hentNavn(self):
        return self._navn




