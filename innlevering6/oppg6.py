# coding=utf-8
"""Dette programmet Spør bruker om navn, alder og hobbyer, som gjennom en klasse blir brukt for å legge til de ulike hobbyene i en liste, og derett skrive ut disse"""

#Oppgavebeskrivelse fra oppgave 6:
#Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal konstruktøren ha en tom liste hobbyer.
#Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i hobbyer-listen.
# Skriv også en metode skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
# Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på metoden skrivHobbyer.
# La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil.
# Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.

#klassen "Person" blir opprettet
class Person:

    #konstruktlr som tar imot "navn" og "alder"
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        #en tom liste opprettes
        self._hobbyer = []

    #Metode som legger til tekst fra parameter til den tomme listen
    def leggTilHobby(self, tekst):
        self._hobbyer.append(tekst)

    #Metode som skriver ut alle hobbyer som er lagt til listen
    def skrivHobbyer(self):
        for x in self._hobbyer:
            print(x)

    #Metode som skriver ut navn, alder og liste med hobbyer
    def skrivUt(self):
        print("Navn:", self._navn)
        print("Alder:", self._alder)
        print("")
        print("Hobbyer:")
        self.skrivHobbyer()

print("----------------------------------------------------------\n")

#to variabler som tar imot input fra bruker
navn = input("Hva er navnet ditt?: ")
alder = input("Hvor gammel er du?: ")

#objekt som kaller opp klassen "Person" med navn og alder-input ovenifra som argumenter.
person = Person(navn, alder)
print("")

#while-loop som spør om bruker ønsker å fortsette å legge til hobbyer
inp = input("Ønsker du å legge til hobby i din liste?: ")
while inp.lower() == "ja":
    hobby = input("Hvilken hobby vil du legge til?: ")
    #kaller opp metoden "leggTilHobby" med input ovenifra som argument, fra klassen "Person" i objektet "person"
    person.leggTilHobby(hobby)
    #input som spør igjen om bruker vil fortsette
    inp = input("Ønsker du å fortsette å legge til?: ")

print("")
#kaller opp metoden "skrivUt()" fra klassen "Person" i objektet "person"
person.skrivUt()

print("\n----------------------------------------------------------")