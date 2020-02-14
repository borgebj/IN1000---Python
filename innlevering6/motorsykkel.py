# coding=utf-8
"""Dette er en klasse som blir importert i filen "testMotorsykkel.py" """
#Klassen "Motorsykkel" blir opprettet
class Motorsykkel:

    #konstruktør som tar imot 3 argumenter (merke, regnr og km)
    def __init__(self, merke, regnr, km):
        self._merke = merke
        self._regnr = regnr
        self._km = km

    #metode som legger til kilometer
    def kjor(self, km):
        self._km += km

    #metode som returnerer motorsykkelens totale kilometerstand.
    def hentKilometerstand(self):
        return self._km

    #metode som skriver ut klassen med gitt argumenter.
    def skrivUt(self):
        print("Merke:",self._merke, "- Registreringsnummer:",self._regnr, "- Kilometerstand:", self._km)

