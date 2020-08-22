# coding=utf-8
from student import Student
from fag import Fag

class Studentsystem:

    def __init__(self):
        self._studentliste = []
        self._fagliste = []

    def hentFil(self, filnavn):
        fil = open(filnavn)
        fag = None
        """
        #leser gjennom filen ovenfor ^
        for x in fil:
            #hvis stjerne er i linjen, legges linjen til i faglisten
            #kan også skrives if linje[0] == "*"
            if "*" in x:
                self._fagliste.append(x)

            #ellers må linjen være en student, og det legges til i studentlisten
            elif not self.sjekkStudent(x):
                #self._studentliste.append(x)
        """

        for linje in fil:
            if linje[0] == "*":
                fag = Fag(linje[1:])
                self._fag.append(fag)
            else:
                stud = self.sjekkStudent(linje.strip())
                if stud == None:
                    stud = Student(linje[:-1])
                    self._studentListe.append(stud)
                fag.leggTilStudent(stud)
                stud.leggTilFag(fag)
        fil.close()

    def sjekkStudent(self, navn):
        for student in self._studentliste:
            #om objektet med metoden (hentStudentNavn - som henter selve navnet i streng) er  det samme som parameteret, returneres studenten.
            if student.hentStudentNavn() == navn:
                #returneres objektet
                return student
        return None

    def finnFag(self, navn):
        for fag in self._fagliste:
            if fag.hentFagNavn() == navn:
                return fag
        return None

    def skrivStudent(self):
        inp = input("Hva heter studenten?: ")
        student = self.finnStudent(inp)
        if student == None:
            print(inp + "finnes ikke i studentsystemet.")
        else:
            student.skrivFagPaaStudent()

    def skrivFag(self):



    def flestFag(self):
        for x in self._studentliste:
