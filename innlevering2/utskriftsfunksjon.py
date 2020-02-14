
"""Dette programmet spør brukeren om navn og bosted. Disse variablene og kommandoene blir lagret i prosedyren kalt for "prosedyre" som blir kalt opp 3 ganger, slik at 3 ganger får skrevet inn navn og bosted"""

#def prosedyre() er starten av prosedyren, og det under er hva som er lagret i prosedyren.
def prosedyre():
#programmet spør brukeren om navn og bosted, og printer ut disse variablene sammen med tekst.
    navn = input("Hva er ditt navn?: ")
    bosted = input("Hvor kommer du fra?: ")
    print("Hei", navn + ",", "du kommer fra:", bosted, "\n")


#Dette vil si at prosedyren blir kalt opp 3 ganger
prosedyre()
prosedyre()
prosedyre()
