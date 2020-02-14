"""Dette programmet spør brukeren om å skrive inn to ulike dager og måneder for to datoer. Programmet sammenligner deretter om den første datoen brukeren skrev inn kommer først i året sammenlignet med den andre, eller om de er like."""

#Variabler som brukeren definerer ved å skrive inn i terminalen. Variablene spør om å skrive to dager og to måneder som er ulike.
dag1 = int(input("Skriv inn dag (tall): "))
maaned1 = int(input("Skriv inn måned (tall): "))
dag2 = int(input("Skriv inn en annen dag (tall): "))
maaned2 = int(input("Skriv inn en annen måned (tall): "))

#Først sjekker programmet om den første måneden er mindre enn den andre, og om den er skrives ut "riktig rekkefølge"

if maaned1 < maaned2:
    print("Riktig rekkefølge!")
#Ellers blir det feil rekkefølge
elif maaned1 > maaned2:
    print("Feil rekkefølge!")
#Hvis månedene er like, må programmet deretter sammenligne dagene for å se hvem som kommer føst, eller om de er like.
elif maaned1 == maaned2:
    if dag1 < dag2:
        print("Riktig rekkefølge!")
    elif dag1 > dag2:
        print("Feil rekkefølge!")
    elif dag1 == dag2:
        print("Samme dato!")
