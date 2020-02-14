# coding=utf-8
"""Dette programmet tar 15 ulike inputs fra brukeren, og bruker denne infoen for å lage en reiseplan, som da brukeren kan slå opp om de ønsker på slutten av programmet."""

#for å bedre oversikt i terminalen.
print("--------------------------------------------------------------------\n")

print("Reiseplan\n")

#variabel som lagrer tom liste.
steder = []

#for løkke som gjør koden 5 ganger (range(5))
for reiseMaal in range(5):
    #input som spør bruker om reisemål, og dermed legges inn i listen "steder." Dette gjøres 5 ganger pga for-løkken.
    sted = input("Skriv inn ditt reisemål: ")
    steder.append(sted)

#to variabler som hver lagrer tomme lister.
klesplagg = []
avreisedatoer = []

#for-løkke som plasserer input fra brukeren i den tomme listen "klesplagg" 5 ganger.
for plaggFor in range(5):
    plagg = input("Skriv inn klesplagg du ønsker å ha med: ")
    klesplagg.append(plagg)

#for-løkke som plasserer input fra bruker i den tomme listen "avreisedatoer" 5 ganger.
for datoFor in range(5):
    dato = input("Skriv inn hvilken dato du ønsker (eks: 11.09.19): ")
    avreisedatoer.append(dato)

#variabelen "reiseplan" blir gjort om til en nøsted liste ved å legge til de 3 andre listenene som nå er fylt.
reiseplan = [steder, klesplagg, avreisedatoer]

print("")

#for løkke som printer ut hver liste i den nøstede listen. "Teller" er indeksen i listen, og økes for hver gang for-løkken utgjør koden under.
for teller in reiseplan:
    print("Liste - ", teller)

print("")

#Input fra bruker lagres i variabel.
i1 = input("Hvilken liste ønsker du å se? (0-2):  ")
#input blir gjort om til integer (tall)
i1 = int(i1)

#om tallet fra brukeren er over eller lik 0 OG mindre eller like lengden på listen - 1, kjøres koden under: gyldig input mellom 0 og lengden på listen - 1
if i1 >= 0 and i1 <= len(reiseplan) - 1:
    print("Listen du valgte er: ", reiseplan[i1])
    print("")

    #ny input som spør brukeren om element i den valgte listen og lagret dette.
    i2 = input("Hvilket element ønsker du å se? (0-4): ")
    i2 = int(i2)

     #om tallet  fra brukeren er over eller lik 0 OG mindre eller lik lengden på listen brukeren valgte minus 1, kjøres koden under.
    if i2 >= 0 and i2 <= len(reiseplan[i1]) - 1:
        #Elementet brukeren valgte i listen brukeren valgte printes ut.
        print("Elementet du valgte er: [", reiseplan[i1][i2], "]")
    else:
        #om lengden ikke passer printes ut ugyldig input
        print("Ugyldig input!")
else:
    print("Ugylidg input")
print("\n--------------------------------------------------------------------")

