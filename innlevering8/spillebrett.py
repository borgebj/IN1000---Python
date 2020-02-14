# coding=utf-8
from random import randint
from celle import Celle
#importerer klassen Celle og randint

#Klassen Spillebrett
class Spillebrett:
    #Konstruktør som tar imot 2 argumenter
    def __init__(self, rader, kolonner):
        #4 instansvariabler som blir definert, 2 av dem definert fra argumentene
        self._rader = rader
        self._kolonner = kolonner
        #tom liste som skal inneholde rutenettet
        self._rutenett = []
        #instansvariabel som inneholder generasjonsnummeret
        self._nr = 0

        #nøsted for-løkke som skal opprette rutenettet
        for x in range(rader):
            #tom liste som skal bli lagt til i rutenett-listen (nøsted-liste)
            list = []
            self._rutenett.append(list)
            for y in range(kolonner):
                #legger til celle-objekt i hver rute i rutenett
                celle = self.generer()
                list.append(celle)


    #instansmetode som skal tegne ut rutenettet, altså tegnene til celle-objektene
    def tegnBrett(self):
        for x in self._rutenett:
            for y in x:
                #end har 3 mellomrom i seg for å skape avstand mellom hver "." og "O"
                print(y.hentStatusTegn(), end="  ")
            #linjeskift for hver liste, slik at det ikke blir en lang linje
            print("|")

    #instansmetode som skal oppdatere rutenettet og generasjonsnummeret
    def oppdatering(self):
        self._nr += 1
        print("Generasjon: ", self._nr)

        #2 lister som inneholder cellene som er døde og skal bli levende
        dodTilLevende = []
        #og cellene som er levende og skal bli død
        levendeTilDod = []

        #2 for løkker som finner koordinater
        for x in range(self._rader):
            for y in range(self._kolonner):

                #variabel som holder på koordinatene til cellen i rutenettet
                celleKoord = self._rutenett[x][y]

                #sjekker om cellen tilknyttet koordinatene er levende eller ikke
                #if gjelder de levende cellene
                if celleKoord.erLevende():
                    #liste som inneholder alle de levende naboen til den levende cellen
                    levendeNaboer = []
                    #for hver nabo:
                    for a in self.finnNabo(x, y):
                        #om naboen er levende, legg til i liste
                        if a.erLevende():
                            levendeNaboer.append(a)
                    #hvis cellen har mindre enn 2 eller mer enn 3 blir det over/underpopulasjon
                    if len(levendeNaboer) < 2 or len(levendeNaboer) > 3:
                        #derfor dør cellen
                        levendeTilDod.append(celleKoord)

                #else gjelder de døde cellene
                else:
                    #liste som inneholder alle de levende naboene til den døde cellen
                    dodesLevendeNaboer = []
                    #for-løkke som gjør følgende for hver nabo
                    for b in self.finnNabo(x, y):
                        #sjekker om naboen er levende
                        if b.erLevende():
                            #legger til levende naboer i egen liste
                            dodesLevendeNaboer.append(b)

                    #sjekker om død celle har akkurat 3 naboer:
                    if len(dodesLevendeNaboer) == 3:
                        dodTilLevende.append(celleKoord)

        #2 for-løkker som oppdaterer cellene som skal dø, og cellene som skal komme tilbake
        for hver in dodTilLevende:
            hver.settLevende()

        for each in levendeTilDod:
            each.settDoed()

    #enkel instansmetode som skal se  gjennom rutenettet og returnere antall levende celler
    def finnAntallLevende(self):
        #variabel for antall levende - oppdateres
        antallLevende = 0
        for x in self._rutenett:
            for y in x:
                #om y (hver i hver liste) er levende:
                if y.erLevende():
                    #oppdaterer variabel
                    antallLevende += 1
        #returnerer variabelen som inneholder et tallz
        return antallLevende

    #Instansmetode som endrer statusen til en celle tilfeldig
    def generer(self) :
        #variabel som tar imot et tilfeldig tall fra 0 til 2
        tall = randint(0, 2)
        #variabel som holder på Celle-objekt fra klassen Celle
        celle = Celle()
        #om variabelen over får 0, settes cellen som levende (altså 0=1/3, som er 30% sjanse)
        if tall == 0:
            celle.settLevende()
        #ellers dør cellen
        else:
            celle.settDoed()
        #celle-objektet returneres (med ny status)
        return celle

    #Metode kopiert fra gruppetime !
    def finnNabo(self, rad, kol):  # Gaar mer nøye gjennom i uke 11
        naboer = []
        for i in range(-1, 2):  # En nabo er enten på raden før, samme rad eller neste rad.
            for j in range(-1, 2):  # På samme måte som rad.
                naboRad = rad + i
                naboKol = kol + j
                gyldig = True
                # sjekker at det ikke er den selv
                if naboRad == rad and naboKol == kol:
                    gyldig = False
                # sjekker at radindex er gyldig
                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False
                # sjekker at kolonneindex er gyldig
                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False
                # hvis det er en gyldig index, saa legger vi til i naboliste:
                if gyldig:
                    naboer.append(self._rutenett[naboRad][naboKol])  # Legger til hundeobjektet
        #returnerer en liste med alle naboene
        return naboer
