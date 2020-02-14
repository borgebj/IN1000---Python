# coding=utf-8
from hund import Hund
#^importerer klassen "Hund" fra filen "hund"

print("--------------------------------\n")

#prosedyre som inneholder koden som skal kjøres
def hovedprogram():
    #objekt som inneholder den importerte klassen med to arumenter
    hundeobjekt = Hund(7, 18)

    #to objekt som kaller opp metoden vekt og alder fra Hund
    hundeobjekt.vekt()
    hundeobjekt.alder()
    print("")

    #skriver ut hva hunden spiser
    print("Hunden spiser -4:")
    #3 objekt som først kallr opp metoden spis med -4 som argument.
    hundeobjekt.spis(-4)
    #andre objekt kaller opp metoden spring
    hundeobjekt.spring()
    #tredje objekt skriver ut den nye vekten til hunden
    hundeobjekt.vekt()

    #skriver ut hva hunden spiser, og gjør det samme som ovenfor
    print("\nHunden spiser 6:")
    hundeobjekt.spis(6)
    hundeobjekt.spring()
    hundeobjekt.vekt()


#kaller prosedyren hovedprogram
hovedprogram()

print("\n--------------------------------")
