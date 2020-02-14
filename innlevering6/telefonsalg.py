# coding=utf-8
"""Dette programmet leser inn fra en tekstfil og skriver ut personen med høyest antall salg, aktive selgere, totale salg og gjennomsnittet på alle salgene"""

print("--------------------------------------------------")

#funksjon som tar imot en fil
def innlesing(filnavn):
    #filen blir åpnet i en variabel
    minFil = open(filnavn)

    #tom ordbok
    dict = {}

    #for-løkke som splitter hver linje i filen, og dermed angir hver bit som er splittet en variabel
    for x in minFil:
        bit = x.split()
        ansatt = bit[0]
        tall = bit[1]
        #bitene som er splittet blir lagt til i den tomme ordboken
        dict[ansatt] = tall

    #for-løkke som gjør alle tall i ordboken om til integer
    for x in dict:
        dict[x] = int(dict[x])
    #ordboken returneres
    return dict


#prosedyre som tar imot en ordbok
def maanedensSalgsperson(ordbok):

    #tall og navn blir satt som tomme verdier, for å senere oppdateres
    tall = 0
    navn = ""

    #for hvert navn i ordboken, sjekk om salget til navnet er høyere enn talv
    for x in ordbok:
        if ordbok[x] > tall:
            #om det er høyere, oppdater navn og tall
            tall = ordbok[x]
            navn = x

    print("\n"+navn, "har det høyeste salget, på",tall, "salg!\n")

#funksjon som tar imot en ordbok
def totaltAntallSalg(ordbok):
    sum = 0
    #for hvert navn i ordboken, legg til tilsvarende salg i variabelen "sum"
    for x in ordbok:
        sum += ordbok[x]
    #returnerer variabelen "sum" etter for-løkken er ferdig
    return sum

#funksjon som tar imot en ordbok
def gjennomsnittSalg(ordbok):
    sum = 0
    #for-løkke som gjør samme som ovenfor, men i tillegg deler antall salg med lengden på ordboken (antall navn) for å finne gjennomsnitt
    for x in ordbok:
        sum += ordbok[x]
    sum = sum / len(ordbok)
    return sum

#prosedyre som inneholder funksjonene og prosedyrene ovenfor
def hovedprogram():
    # variabel som holder returnverdien til funksjon(innlesing)
    var = innlesing("salgstall.txt")
    maanedensSalgsperson(var)
    print("Aktive selgere denne måneden:",len(var))
    print("Total antall salg:", totaltAntallSalg(var))
    print("Gjennomsnitt på salgene:", gjennomsnittSalg(var))


#prosedyren kalles opp
hovedprogram()

print("\n--------------------------------------------------")



