# coding=utf-8
"""Dette programmet spør brukeren om deres alder, og endrer billettprisen deres avhengig av hvor gammel de er. Koden blir tatt vare på i en prosedyre som blir kalt opp 4 ganger"""

#Prosedyre som spoer brukeren om alderen deres.
def prosedyre():
    alder = int(input("Hva er alderen din? (i tall): "))
    billettpris = 0
#Om bruker skriver inn verdier som er meningsløse eller andre verdier enn programmet ber om, som f.eks. bokstaver, vil det (i tilfellet med bokstaver) føre til en feilmelding.
#Om brukeren velger å skrive inn en absurd høy verdi som for eksempel at brukeren 1 000 000 år gammel, vil programmet bare gå gjennom if-setningene og endre variabelen til den som passer. Siden 1 000 000 er over 63, vil variabelen da få verdien 35.
#Siden inputen har "int" vil det da si at den kun aksepterer heltall, og er også hvorfor programmet spør om et tall fra brukeren.

#om bruker er yngre enn 17 år, blir billettprisen 30 kroner.
    if alder < 17:
        billettpris = 30
#om bruker er eldre enn 17 år, blir billettprisen 50 kroner.
    elif alder > 17 and alder < 63:
        billettpris = 50
#om bruker er 63 år eller eldre blir billettprisen 35 kroner.
    elif alder >= 63:
        billettpris = 35

#printer ut tekst sammen med billettprisen etter programmet har sjekket alderen.
    print("Bilettprisen blir:",billettpris,"kroner.\n")

#prosedyren blir kalt 4 ganger.
prosedyre()
prosedyre()
prosedyre()
prosedyre()
