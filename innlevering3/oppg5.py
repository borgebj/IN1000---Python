# coding=utf-8
"""Dette programmet inneholder 2 ulike programmer. Den ene (a) er en liste med beboere på et sykehjem, og informasjon om deres frokost, lunsj og mdidag. Her kan brukeren også legge til nye beboere og deres måltid. Det andre programmet (b) er en quiz som bruker if-setninger og lister for å se om brukeren svarer riktig eller galt"""

#Oppgave 5
#a) Det første du skal gjøre er å dele inn programmet i 2 deler ved hjelp av if-setninger. Programmet skal spørre brukeren om de ønsker å se oppgave a eller b, og avhengig av hva de velger skal programmet vise dem oppgaven de skriver inn.
#Dermed skal du (i oppgave a-delen av programmet) utvide oppgave 4 slik at programmet nå også kan spørre brukeren om de ønsker å registrere en ny bruker etter å ha spurt dem om navn til beboer. Dette skal vaere i sin egen prosedyre.
#Listen til den nye registrerte personen skal deretter bli printet ut til terminalen, og den første prosedyren skal bli kjørt på nytt, slik at brukeren kan søke opp den nye registrerte personen.

#b) I b-delen av programmet skal du lage en mini-quiz som tar i bruk både if-setninger, og som også inneholder lister med riktige eller gale svar.
#Quizen skal gi tilbakemelding til brukeren om de har riktig eller feil svar.

print("\nDenne oppgaven er delt i do deler (a og b)")
oppg = input("Hvilken oppgave ønsker du aa se? (a/b): ")

if oppg.lower() == "a":
    #Nøstede ordbøker som inneholder beboer for sykehjem og frokost, lunjsen, og middagen deres.
    sykehjem = {"Kari Nordmann":{"frokost":"2 brødskiver med ost", "lunsj":"En halv grandiosa pizza", "middag":"Ribbe"}}

    print("\n- Program for sykehjem - ")
    #Sjekker lengden (len) på listen, og skriver ut hvor mange beboere er på sykehjemmet.
    print("Antall beboere på sykehjem:", len(sykehjem))

    #Prosedyre blir definert som inneheholder if-setninger og variabel som hentes fra brukeren, og som dermed blir sjekket av programmet om input fra brukeren (altså det beboeren skrev inn) er med i ordboken ovenfor.
    def hjem():

        #variabelen beboer blir satt av brukeren
        beboer = input("\nSkriv inn navn til beboer: ")

        # om beboer (satt av brukeren) er inne i ordboken ovenfor, vil programmet skrive ut matplanen deres.
        if beboer in sykehjem:
            print("\nMatplanen til",beboer)
            print("Frokost: "+sykehjem[beboer]["frokost"])
            print("Lunsj: "+sykehjem[beboer]["lunsj"])
            print("Middag: "+sykehjem[beboer]["middag"])

        # ellers vil de få bedskjed om at beboeren ikke er registrert.
        else:
            print("Beboer ikke registrert")

#prosedyre som inneholder kode for å registrere ny beboer, og deres matplan.
    def registrer():
        #variabel som spoer om bruker ønsker å registrere ny beboer
        reg = input("\nØnsker du å registrere en ny beboer? ")

        #Denne sjekker om bruker ønsker å registere. .lower gjør om bokstavene fra store til små for å unngå problemer med store og små bokstaver.
        if reg.lower() == "ja":
            #hvis bruker svarer ja, skriver bruker inn frokost, lunsj og middag til den nye beboeren brukeren skrev inn.
            nybeboer = input("\nHva er navnet til ny beboer? ")
            frokost = input("Hva skal denne personen ha til frokost? ")
            lunsj = input("Hva skal denne personen ha til lunsj? ")
            middag = input("Hva skal denne personen ha til middag? ")

            #her legges til verdiene skrevet inn av brukeren innenfor mapper i den nye registrerte brukeren.
            sykehjem[nybeboer] = {"frokost":frokost, "lunsj":lunsj, "middag":middag}
            print("Ny beboer registrert!")

            #Sjekker lengde på liste og printer ut antall beboere.
            print("\nAntall beboere på sykehjem:",len(sykehjem))

            #Denne blir kjørt etter at brukeren har valgt å registrere ny bruker.
            hjem()

        #hvis bruker svarer nei printes ut "den er grei" til terminalen.
        elif reg.lower() == "nei":
            print("Den er grei")
        #hvis brukeren skriver noe annet, "det forstod jeg ikke" printes ut"
        else:
            print("Det forstod jeg ikke")

    #Prosedyren som spør brukeren om navn til beboer på sykehjem går i gang.
    hjem()
    #Prosedyren som spør brukeren om de ønsker å registrere beboer går i gang. Inne i denne kjøres også "hjem()" til slutt.
    registrer()

#hvis brukeren svarer b på første input, går quizen i gang.
elif oppg.lower() == "b":
    #spør brukeren om de ønsker å delta i quizen.
    quiz = input("\nØnsker du å delta i en quiz? (ja/nei): ")

    #hvis brukeren svarer ja, starter quizen.
    if quiz.lower() == "ja":
        print("\nHei, velkommen til denne quizen. Her kommer vi til å spørre deg om noen få spørsmål, og du kan svare det du tror er riktig.")
        print("Du vil få tilbakemelding om svaret ditt er riktig eller ikke.""\n")

        #kode som får programmet til å vente i 4 sekunder før neste handling skjer.
        import time
        time.sleep(4)

        #første spørsmaal går i gang.
        quiz1 = input("\nNevn en slags type interaksjon: ")
        #liste som inneholder de ulike svarene.
        interaksjon = ["instruerende", "manipulerende", "konverserende", "eksplorerende", "responderende"]

        #hvis input fra brukeren er "in"/i listen, printes ut korrekt.
        if quiz1.lower() in interaksjon:
            print("Det er korrekt! Det er 5 ulike typer interaksjon")
        #hvis ikke har brukeren feil.
        else:
            #printer ut svaret sammen med string "er ikke korrekt"
            print(quiz1,"er ikke korrekt")

        #programmet venter i 2 sekunder
        time.sleep(2)

        #andre spørsmaal går i gang.
        quiz2 = input("\nHva er hovedstaden i Saudi Arabia? ")

        #her brukes ikke en liste, men programmet sjekker om input er lik svaret (riyadh).
        if quiz2.lower() == "riyadh":
            print("Det er korrekt! Riyadh er hovedstaden i Saudi Arabia.")
        else:
            print(quiz2, "er ikke korrekt")

        time.sleep(2)

        quiz3 = input("\nNevn ett type bilmerke laget i Tyskland: ")
        tyskland = ["audi", "volkswagen", "bmw", "porsche", "mercedes-Benz", "mercedes", "opel"]

        if quiz3.lower() in tyskland:
            print("Det er korrekt!")
        else:
            print(quiz3, "er ikke korrekt")

        time.sleep(2)

        quiz4 = input("\nNevn en av Norges statsministere fra 2000-tallet opp til nå (2000-2019): ")
        statsminister = ["kjell magne bondevik", "jens stoltenberg", "erna solberg"]

        if quiz4.lower() in statsminister:
            print("Det er korrekt. Fra omtrent 2000 til 2019 har både Jens Stoltenberg og Kjell Magne Bondevik vært statsminister 2 ganger.")
        else:
            print(quiz4, "er ikke korrekt")

        time.sleep(2)

        #programmet printer ut en melding på slutten.
        print("\nTakk for at du deltok i quizen vaar!")
    #printes ut om brukeren svarer nei.
    elif quiz.lower() == "nei":
        print("Den er grei")

    else:
        print("Det forstod jeg ikke")

else:
    print("Ingen oppgave valgt")


