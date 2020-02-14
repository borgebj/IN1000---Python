import time
# coding=utf-8
"""Dette programmet tar inn en tekstfil for en skredder, spør skredderen om hva de vil vite målet til, så printer programmet ut antall tommer på målet og konverterer dette til centimeter med en funksjon"""
#Lag et beregningsprogram for skreddere med en funksjon som leser inn en fil (skredder.txt), der hver linje beskriver et navn på et mål og selve målet i tommer.
#a) Del opp hver linje i tekstfilen din i en funksjon. Bruk funksjonen .split(). Dermed legg inn verdiene som nå er splittet opp i en ordbok, hvor navnet på målet blir nøkkelverdien, mens selve målet i tommer blir innholdsverdien. Returner så ordboken på slutten av funksjonen.

#b) Ta i bruk den tidligere funksjonen "tommerTilCm" sammen med en ny prosedyre for å nå spørre brukeren om hvilket mål de ønsker å vite. Den nye prosedyren skal, utifra ordboken som ble returnert i a), skrive ut antall tommer for målet brukeren skrev inn.
#Den tidligere funksjonen "tommerTilCm" skal bli brukt for å konvertere antall tommer på målet brukeren ønsket å se om til centimeter, dette skal da blir printet ut også utifra funksjonen.

#c)Hvis brukeren skriver feil eller noe annet på hva de ønsker å se, skal du kode slik at programmet spør om brukeren vil legge disse til i listen sammen med hvor mange tommer, og skal så legge disse til i ordboken. Funksjonen "tommerTIlCm" skal også bli brukt for å konvertere verdien brukeren gir.

print("-------------------------------------------------------------\n")

#funksjon som legger inn mål og tommer fra tekstfilen "skredder.txt" og putter disse som nøkkelverdi og innholdsverdi i en ordbok.
def skredder():

    #tom ordbok
    skredd = {}
    #variabelen "skredder" innholder alt fra tekstfilen.
    skredder = open("skredder.txt")

    #for-løkke som splitter linjene fra tekstfilen og legger disse inn i en ordbok.
    for x in skredder:
        #hver linje blir splittet, for å deretter bli satt inn i en ordbok.
        linje = x.split()
        a = linje[0].lower()
        b = linje[1].lower()
        #første verdi i hver linje (a) blir gjort om til nøkkelverdi, mens andre verdi i hver linje (b) blir innholdsverdi.
        skredd[a] = b
    #funksjonen returnerer selve ordboken.
    return skredd

#funksjon fra oppgave 1 som gjør tommer om til centimeter.
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    #selve konverteringen, ganger antall tommer med 2.54
    cm = antallTommer * 2.54
    print("\nKonvertering fra tommer til centimeter:")
    print("Resultat av konvertering:", cm, "centimeter.")
    #returnerer konverteringen
    return cm

#prosedyre som bruker ordboken fra funksjonen "skredder()"
def prosedyre():
    #variabelen "ordbok" blir definert som ordboken fra funksjonen "skredder()", som returnerte en ordbok.
    ordbok = skredder()

    #tekst som forteller bruker hva de kan velge mellom, og input om hva brukeren ønsker å se.
    print("Mål å velge mellom: 'skulderbredde'   'halsvidde'   'livvidde'")
    maal = input("Hvilket mål vil du vite? ")

    print("")

    #if-setning som sjekker om input fra bruker er i ordboken eller ikke.
    if maal in ordbok:
        #innholdsverdien som tilhører nøkkelverdien gitt av brukeren blir gjort om til float.
        ordbok[maal] = float(ordbok[maal])
        #programmet printer ut antall tommer til målet brukeren ønsket å se.
        print("Målet til", maal, "er:", ordbok[maal], "tommer.")

        #funksjonen "tommerTilCm" blir kalt opp med input fra bruker som argument.
        tommerTilCm(ordbok[maal])
    #om input fra brukeren ikke er i ordboken, sier programmet ifra, og spør om de ønsker å legge den til.
    else:
        print(maal, "finnes ikke i ordboken din.")

        time.sleep(1)

        inp1 = input("Ønsker du å legge den til? ")

        #if-setning som ser om brukeren ønsker å legge til ny verdi eller ikke.
        if inp1.lower() == "ja":
            #spør om hvor mange tommer og gjør dette om til float.
            inp2 = input("Hvor mange tommer? ")
            inp2 = float(inp2)
            #legger til mål og tommer i ordbok.
            ordbok[maal] = inp2
            #kaller opp funksjonen "tommerTilCm" for de nye verdiene.
            tommerTilCm(ordbok[maal])

        elif inp1.lower() == "nei":
            print("Greit.")
        else:
            print("Jeg forstod ikke det.")


#prosedyren blir kalt opp.
prosedyre()


print("\n-------------------------------------------------------------")
