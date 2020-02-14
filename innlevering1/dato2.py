
"""Dette programmet spør brukeren om to ulike datoer, som dermed blir sammenlignet for å se om første dato kommer først i året enn andre dato, eller om de er like"""

#Eksempel forteller brukeren hvordan de skal skrive inn dato
print("Eksempel på hvordan du skriver inn dato: 7. april -> 74")
dato1 = input("Skriv inn en dato: ")
dato2 = input("Skriv en annen dato: ")

#dato1 og dato2 hentet inn fra brukeren sammenlignes for å se om dato1 er lavere enn dato2.
if dato1 < dato2:
    print("Riktig rekkefølge")
#Hvis dato1 ikke er lavere enn dato2, sammenlignes om dato1 er høyere enn dato2 her.
elif dato1 > dato2:
    print("Feil rekkefølge")
#Hvis verken dato1 er lavere enn dato2, eller dato1 er høyere enn dato2, er de to like og "Samme dato!" printes ut.
else:
    print("Samme dato")
