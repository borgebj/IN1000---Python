from fag import Fag

#oppg 2
class Student:

    def __init__(self, navn):
        self._navn = navn
        self._liste = []

    #fag = objekt
    def leggTilFag(self, fag):
        self._liste.append(fag)

    def hentAntallFag(self):
        return len(self._liste)

    def hentStudentNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print(self._navn)
        for x in self._liste:
            print(x.hentFagNavn)

