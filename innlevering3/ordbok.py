# coding=utf-8
"""Dette programmet oppbevarer ordbøker, legger til mapper og verdien inne i disse ordbøkene ved hjelp av input fra brukeren, og dermed printer dette ut"""

#Lager ordbok kalt "butikk" som innholder varer og deres tilsvarende priser.
butikk = {"melk":14.9,"brod":24.9,"yoghurt":12.9,"pizza":39.9}

#printer ut ordboken
print(butikk)

#Her henter programmet input fra brukeren om både vare og tilsvarende pris på 2 varer.
vare1 = input("\nHvilken vare ønsker du å legge til? ")
pris1 = float(input("Hvor mye skal varen koste? "))
vare2 = input("\nHvilken vare ønsker du å legge til? ")
pris2 = float(input("\nHvor mye skal varen koste? "))

#legger til input fra brukeren inn i ordboken.
butikk[vare1] = pris1
butikk[vare2] = pris2

#printer ut ny ordbok med varer og priser hentet fra bruker.
print(butikk)
