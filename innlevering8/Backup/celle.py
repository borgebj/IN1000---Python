# coding=utf-8

#klasse Celle
class Celle:
    #Konstrktøren til klassen "Celle". Statusen er satt til "død" uten endring
    def __init__(self):
        self._status = "død"

    #Instansmetode som endrer statusen til cellen til "død"
    def settDoed(self):
        self._status = "død"

    #Instansmetode som endrer statusen til cellen til "levende"
    def settLevende(self):
        self._status = "levende"

    #Instansmetode som sjekker om cellen er død eller levende, og returnerer True/False
    def erLevende(self):
        #om cellen er levende, returneres True
        if self._status == "levende":
            return True
        #ellers er cellen død om False returneres
        elif self._status == "død":
            return False

    #Instansmetode som kalles på et celle-objekt for å få tegnet til cellen, avhengig av om den er død eller levende
    def hentStatusTegn(self):
        #om metoden "erLevende" returnerer True:
        if Celle.erLevende(self):
            #vil bokstaven "O" returneres
            return "O"
        #ellers må cellen være død, og punktum returneres
        return "."
