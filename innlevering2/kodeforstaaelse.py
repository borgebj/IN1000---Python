"""dette programmet tar input for et heltall og sjekker om heltallet hentet fra brukeren er mindre enn 10 eller ikke"""

#1) Er dette lovlig kode?
#- Nei, det er ikke. Grunnen for at det ikke er lovlig kode er fordi + tegnet som er skrevet i print er for å sette sammen tekstself.
#Koden vil legge sammen en variabel som er definert som et heltall sammen med tekst, og vil dermed bety at koden ikke vil fungereself.
#For at koden skal fungere, må enten + (pluss) byttes ut med , (komma), ellers må det skrives: print(str(b) + "hei") for at det skal printes ut riktig.

#2) Hvilken problemet kunne vi møte på når vi kjører denne koden?
#- Det vil komme feilmelding som da vil si at det er en feil på linjen med print, og det vil kome melding "TypeError: unspported operand type(s) for +: "int" and "str"

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
