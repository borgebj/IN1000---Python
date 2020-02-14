# coding=utf-8
"""Dette programmet tar vare på matplanen til beboere på et sykehjem inne i en nøsted ordbok. Etter input fra brukeren sjekker programmet om den gitte brukeren er registrert eller ikke, og skriver ut matplanen avhengig av dette"""

#Nøstede ordbøker som inneholder beboer for sykehjem og frokost, lunjsen, og middagen deres.
sykehjem = {"Kari Nordmann":{"frokost":"2 brødskiver med ost", "lunsj":"En halv grandiosa pizza", "middag":"Ribbe"}}

#prosedyre som inneheholder if-setninger og variabel som hentes fra brukeren, og som dermed blir sjekket av programmet om input fra brukeren (altså beboeren skrevet inn) er med i ordboken ovenfor.
def hjem():
    #variabelen beboer blir satt av brukeren
    beboer = input("\nSkriv inn navn til beboer: ")

#om beboer (satt av brukeren) er inne i ordboken ovenfor, vil programmet skrive ut matplanen deres.
    if beboer in sykehjem:
        print("\nMatplanen til kari nordmann:")
        print("Frokost: "+sykehjem["Kari Nordmann"]["frokost"])
        print("Lunsj: "+sykehjem["Kari Nordmann"]["lunsj"])
        print("Middag: "+sykehjem["Kari Nordmann"]["middag"])
#ellers vil de få bedskjed om at beboeren ikke er registrert.
    else:
        print("Beboer ikke registrert")

#setter i gang prosedyren
hjem()

#oppgave 3
#a) Brukernavn på alle IN1000 studentene
#- jeg ville brukt ordbok, fordi da kan jeg knytte studentens ekte navn med brukernavnet. eks: IN1000 = {"Arne Koll":"arnekoll", "Kari Nordmann":"karinor"}

#b) Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
#- jeg ville igjen brukt ordbok, men heller en nøsted orbok for å få plass til all informasjonen. eks: oblig3 = {"Arne Koll":{"brukernavn":"arnekoll", "poeng":"5/5"}}

#c) Alle vinnere i Lotto siste år (kun navn)
#- jeg ville brukt mengde fordi vi trenger bare en verdi (navnet), og i motsetning til vanlig liste skal det kun være en av samme person (kun ulike verdier). eks: lottovinnere = [Arne, kari, Børge]

#d) All mat noen gjest i et selskap er allergisk mot (for å planlegge menyen)
#- jeg ville brukt en vanlig liste for å liste opp all maten som ulike gjester er allergisk mot. eks: allergi = ["fisk", "Nøtter", "Egg", "Tacokrydder"]
