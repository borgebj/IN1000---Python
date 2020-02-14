# coding=utf-8
#klassen "Hund" blir opprettet
class Hund:

    #Konstruktør som har to parametre, alder og vekt
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        #metthet er allerede satt på 10
        self._metthet = 10

    #metode som skriver ut alderen til hunden
    def alder(self):
        print("Alderen til hunden:", self._alder)

    #metode som skriver ut vekten til hunden
    def vekt(self):
        print("Vekten til hunden:", self._vekt)

    #metode som sjekker mettheten til hunden, og endrer vekten.
    def spring(self):
        if self._metthet < 5:
            self.vekt -= 1

    #metode som tar imot et heltall
    def spis(self, heltall):
        #heltall blir lagt til metthet
        self._metthet += heltall

        #om metthet er større en 7 legges til 1 på vekten
        if self._metthet > 7:
            self._vekt += 1
