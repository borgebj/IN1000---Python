# coding=utf-8
"""Dette programmet inneholder 2 program, hvor den ene """
import random
import time
#Oppgave 6
#1) lag et program som bruker for-løkker og ordbøker for å ta input fra bruker, navn og fødselsdato, og legger dette inn i en ordbok.
# Programmet skal deretter spørre bruker om navn, og deretter printe ut tilsvarende fødselsdato og navn.

#2) lag dermed et program som tar i bruk av for-løkker, while-løkker og if-setninger for å lage et automatisert bingospill.
#radene i bingospillet skal bli generert automatisk av programmet, og hvert tall skal være unike. For å gjøre dette trenger du å bruke "import random", men ta gjerne også i bruk "import time"

#3) leg til slutt disse to programmene i hver sin prosedyre som brukeren kan velge mellom på starten av programmet.


#for å bedre oversikt i terminalen.
print("--------------------------------------------------------------------\n")

def bursdagsProg():
    #tom ordbok
    bursdager = {}

    print("")

    #variabel som lagrer verdi fra bruker
    svar = input("Hvor mange venner ønsker å du notere ned bursdag til? ")
    svar = int(svar)

    print("")

    #for løkke som spør bruker navn og fødselsdato antall ganger brukeren ønsker, og legger den i ordboken.
    for listeTall in range(svar):
        navn = input("Skriv inn navn: ")
        bursdag = input("Skriv inn fødselsdato: ")
        bursdager[navn.lower()] = bursdag.lower()
        print("")

    #variabel lagrer verdi fra bruker, som brukes i if-setning.
    inp = input("Hvem ønsker du å vite fødselsdagen til? ")

    #if-setning som sjekker om verdien fra brukeren er i ordboken, og printer deremed ut det.
    if inp.lower() in bursdager:
        print("Fødselsdatoen til", inp, "er", bursdager[inp], "\n")
    elif inp.lower() == "ingen":
        print("Greit\n")
    else:
        print("Denne personen er ikke i listen.\n")

    spsr = input("Ønsker du å se listen din? ")

    #if-setning som sjekker om bruker har svart ja/nei/uleselig, og printer ut ordbok.
    if spsr.lower() == "ja":
        print("Listen din - ", bursdager)
    elif spsr.lower() == "nei":
        print("OK")
    else:
        print("Det fikk jeg ikke med meg.")

def prog2():

    print("\n--------BINGO--------")

    #en tom liste hvor brukte tall legges til
    brukt = []

    for i in range(5):
        #en tom liste som skal opprettes 5 ganger
        rad = []

        #for-løkke som lager tilfeldige tall 5 ganger (range(5) og putter disse i listen som blir opprettet 5 ganger.
        for e in range(5):
            tall = random.randint(10, 99)

            #while-løkke som sjekker om den tilfeldig-genererte tallet er brukt før eller ikke.
            while tall in brukt:
                #om det er brukt, lages det på nytt igjen.
                tall = random.randint(10, 99)
            #tallet legges til i listen "brukt" og listen "rad"
            brukt.append(tall)
            rad.append(tall)
            #programmet venter i 0.04 sekunder for å legge til en liten animasjon.
            time.sleep(0.04)
        #raden printes 5 ganger
        print(rad)

    print("---------------------")

    time.sleep(2)
    x = 0
    #en tom liste
    mineTall = []

    #tekst printes ut som forklarer programmet for brukeren
    print("\nBingo vil nå starte og terningen vil bli kastet")
    print("For å vinne trenger du å ha 3 av tallene som blir kastet")
    time.sleep(3)

    #while-løkke som, mens x er under eller lik 5, kaster en terning fra 10 til 99 5 ganger.
    while x <= 5:
        kast = random.randint(10, 99)
        print("\nKast nr", x, "ble", kast)
        #1 blir lagt til x for hver gang dette skjer
        x += 1
        time.sleep(1)

        #if-setning som sjekker om tallet er i listen "brukt" eller ikke. Om den er, har brukeren tallet.
        if kast in brukt:
            print("Du har dette tallet!")
            #tallet blir lagt til i listen "mineTall"
            mineTall.append(kast)
        else:
            print("Du har ikke dette tallet.")
        time.sleep(2)

    #if-setning som sjekker om lengden av listen "mineTall" er 3 eller høyere. Dersom dette er sant, vinner brukeren.
    if len(mineTall) >= 3:
        print("\nDu har vunnet bingospillet mitt! Gratulerer!.")
    else:
        print("\nDu har tapt bingospillet.")


#input fra bruker.
delOppg = int(input("Program 1 eller 2 : "))

#if-setning som kjører enten første eller andre prosedyre.
if delOppg == 1:
    bursdagsProg()
#ellers om input er 2, starter andre prosedyre.
elif delOppg == 2:
    prog2()

print("\n--------------------------------------------------------------------")
