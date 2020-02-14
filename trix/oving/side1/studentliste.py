from time import sleep

class Student:

    def __init__(self, navn, brukernavn, tlf):
        self._navn = navn
        self._brukernavn = brukernavn
        self._tlf = tlf

    def printInfo(self):
        print("- Navn:",self._navn)
        print("- Brukernavn:",self._brukernavn)
        print("- Telefonnummer:",self._tlf)


ordbok = {}

def hovedprogram():

    navn1 = "Borge"
    navn2 = "Bjarne"
    navn3 = "Kols"
    stud1 = Student(navn1,"borgebj", 46793400)
    stud2 = Student(navn2, "bjarn", 86472298)
    stud3 = Student(navn3, "kolsaas", 22334411)

    ordbok[navn1.lower()] = stud1
    ordbok[navn2.lower()] = stud2
    ordbok[navn3.lower()] = stud3

    for x in ordbok:
        print("---------------------------")
        ordbok[x].printInfo()
        sleep(0.7)
    print("----------------------------\n")


    #oppgave e)
def sjekkNavn(navn):
    print("")
    if navn in ordbok:
        sleep(0.5)
        print("Studentinfo til",str(navn)+":")
        ordbok[navn].printInfo()
    else:
        sleep(0.2)
        print("Denne studenten finnes ikke i listen")
    print("")


def leggTilStudent():
    navn = input("Navn?: ")
    brukernavn = input("Brukernavn?: ")
    tlf = input("Telefonnummer?: ")

    ordbok[navn.lower()] = Student(navn, brukernavn, tlf)

    sleep(0.5)
    print("\n----------------------------")
    print("Studentinfo til", navn)
    ordbok[navn.lower()].printInfo()
    print("----------------------------")



hovedprogram()

sleep(1)
inp = input("Hvilken student vil du soke etter?: ")
sjekkNavn(inp.lower())

inp = input("Onsker du a legge til studenter?: ")
if inp.lower() == "ja":
    leggTilStudent()
