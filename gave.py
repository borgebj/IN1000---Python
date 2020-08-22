# coding=utf-8
class Gave:

    def __init__(self, navn, pris):
        #streng
        self._gaveNavn = navn
        #flytall
        self._gavePris = pris

    def gavePris(self):
        return self._gavePris

    def gaveNavn(self):
        return self._gaveNavn

    def __str__(self):
        return "Navn på gaven: "+self._gaveNavn+"\n"+"pris på gaven: "+str(self._gavePris)





