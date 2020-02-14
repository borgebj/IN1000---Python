import time
# coding=utf-8
"""Dette programmet inneholder 2 funksjoner, en while-løkke og if-setninger. Funksjonene legger sammen to ord fra brukeren, og skriver ut alle elementene i listen"""

#variabelen "mineOrd" blir definert som en tom liste.
mineOrd = []

#en funksjon som legger sammen første og andre parameter, og returnerer summen.
def slaaSammen(x, y):
    sammen = x + y
    return sammen

#en funksjon som skriver ut hvert element i den gitte parameteren (som skal være en liste)
def skrivUt(y):
    for x in y:
        print(x)

#variabel som tar vare på input fra brukeren.
inp = input("\nØnsker du å starte programmet?: ")

#While-løkke som fortsettere med mindre input er "nei".
while inp.lower() != "nei":

    ks = input("Skriv inn bokstav (i / u / s): ")

    #if-setninger som sjekker om input fra bruker (ovenfor) er enten bokstaven i, u eller s.
    if ks.lower() == "i":
        print("")
        #ber brukeren om input 2 ganger.
        streng1 = input("Skriv inn et ord: ")
        streng2 = input("Skriv inn et annet ord: ")
        #slår sammen disse ordene gjennom funksjonen "slaaSammen(streng1, streng2), og legger dette i den tomme listen gjennom "mineOrd.append(funksjonen(parametre))
        mineOrd.append(slaaSammen(streng1, streng2))
        #spør brukeren om de ønsker å fortsette, knyttes til while-løkken.
        inp = input("\nØnsker du å fortsette?: ")

    elif ks.lower() == "u":
        print("")
        #funksjonen skrivUt(y) skriver ut hvert element i den gitte parameteren "mineOrd", som er en tom liste som brukeren fyller.
        skrivUt(mineOrd)
        inp = input("\nØnsker du å fortsette?: ")

    elif ks.lower() == "s":
        #om brukeren skriver "s", blir inputen som holder while-løkken gående gjort om til "nei", slik at den stopper.
        print("\nDen er grei")
        inp = "nei"
    else:
        #om brukeren ikke skriver enten i, u eller s, printes ut "forstår ikke"
        print("\nDen forstod jeg ikke, prøv igjen")
        time.sleep(1)

# - utenfor løkken - det printes ut "Ok - programmet vil ikke starte"
print("\nOK - Programmet vil ikke starte")
