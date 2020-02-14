"""Dette er et quiz-program som begynner med beskrivelse og dermed spør brukeren om de ønsker å delta eller ikke. Om de svarer ja starter quizen med 5 ulike spørsmål som gir tilbakemelding avhengig av hva brukeren svarer"""
#Oppgavetekst
#- Laget et program som fungeren som en quiz, hvor programmet spør brukeren om diverse spørsmål som du bestemmer selv. Oppgaven har med beslutninger å gjøre, så du må altså bruke if/else setningerself.
#Du skal starte programmet med å spørre om brukeren ønsker å delta eller ikke, hvor du skal både if, elif og else.
#Under hvert spørsmål skal det komme tilbake en tilbakemelding til brukeren om de har svart riktig eller feil.
#Når brukeren svarer feil, skal du legge til variabelen som blir definert av brukeren gjennom input sammen med tilbakemeldingstekstenself.
#Samtidig som om du lager if/else-setningene skal på hvertfall ett av spørsmålene ha flere ulike svar, men også muligheten til å skrive ordet både stor og liten bokstav.




print("\nVelkommen til dette quiz-programmet. Her spør vi deg noen spørsmål, og dermed tester DEG om du kan dette eller ikke.")
print("Tilbakemelding vil bli gitt om svaret er riktig eller feil.")

start = input("\nHvis du ønsker å delta, skriv ja. Hvis du ikke ønsker å delta, skriv nei: ")

if start == "ja" or start == "Ja":

#Linjeskifte
    print("\n")

#Spørsmål 1 - Svares riktig printes ut tilbakemelding om at det ble riktig, samtidig som litt fakta. Ellers printes ut variabelen sammen med tilbakemelding som forteller at svaret er feil.
    sps1 = input("- Hva heter den største planeten i vårt solsystem?: ")
    if sps1 == "Jupiter" or sps1 == "jupiter":
        print(" Det er riktig! Jupiter er størst, med areal på 6,142 milliarder kvadratkilometer")
    else:
        print("",sps1, "er ikke riktig, ellers er det skrevet feil")

#Linjeskifte
    print("\n")

#Spørsmål 2 - Svares riktig printes ut tilbakemelding om at det ble riktig, samtidig som litt fakta. Ellers printes ut variabelen sammen med tilbakemelding som forteller at svaret er feil.
    sps2 = input("- På internett, hva står WWW for når du f.eks. skriver inn en nettside?: ")
    if sps2 == "World Wide Web" or sps2 == "world wide web" or sps2 == "World wide web":
        print(" Det er riktig")
    else:
        print("", sps2,"er ikke riktig, ellers er det skrevet feil")

#Linjeskifte
    print("\n")

#Spørsmål 3 - Svares riktig printes ut tilbakemelding om at det ble riktig, samtidig som litt fakta. Ellers printes ut variabelen sammen med tilbakemelding som forteller at svaret er feil.
    sps3 = input("- Hva skal det nye fylket rundt Oslo hete?: ")
    if sps3 == "Viken" or sps3 == "viken":
        print(" Det er riktig! Viken kommer til å bli det nye megafylket som kommer i 2020")
    else:
        print("", sps3,"er ikke riktig, ellers er det skrevet feil")

#Linjeskifte
    print("\n")

#Spørsmål 4 - Svares riktig printes ut tilbakemelding om at det ble riktig, samtidig som litt fakta. Ellers printes ut variabelen sammen med tilbakemelding som forteller at svaret er feil.
    sps4 = input("- Nevn en slags type interaksjon: ")
    if sps4 == "Instruerende" or sps4 == "instruerende" or sps4 == "Konverserende" or sps4 == "konverserende" or sps4 == "Manipulerende" or sps4 == "manipulerende" or sps4 == "Eksplorerende" or sps4 == "eksplorerende" or sps4 == "Responderende" or sps4 == "responderende":
        print(" Det er riktig! Det finnes 5 ulike typer for interaksjon")
    else:
        print("",sps4,"er ikke riktig, ellers er det skrevet feilSSS\n")

#Elif og else går i gang hvis brukeren enten skriver nei/Nei, eller noe helt annet.
elif start == "nei" or start == "Nei":
    print("Greit")

else:
    print(" Jeg skjønte ikke det helt")
