from student import Student

#oppg 1
class Fag:

    def __init__(self, navn):
        self._navn = navn
        self._liste = []

    #sutdent er et objekt
    def leggTilStudent(self, student):
        self._liste.append(student)

    def hentAntallStudenter(self):
        return len(self._liste)

    def hentFagNavn(self):
        return self._navn

    def skrivStudenterVedFag(self):
        print(self._navn)
        for x in self._liste:
            print(x.hentStudentNavn())