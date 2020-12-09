
class Student:
    def __init__(self, navn):
        self._navn = navn
        self._emner = []

    def leggTilEmne(self, emne):
        self._emner.append(emne)

    def skrivUtEmner(self):
        for emne in self._emner:
            print(emne)


stud1 = Student("borge")

ordbok = {"IN1000": 1, "IN2000": 2}

stud1.leggTilEmne(ordbok["IN1000"])

stud1.skrivUtEmner()

string = "Gruppe1"
print(string[len(string)-1])