# coding=utf-8
from spillebrett import Spillebrett
from celle import Celle
#importerer de 2 klassene

#pr
def main():

    print("")

    #2 inputs som spør bruker hvor stør de ønsker rutenettet
    inp1 = int(input("Hvor mange rader? (bortover): "))
    inp2 = int(input("Hvor mange kolonner? (nedover): "))
    #kaller opp klassen Spillebrett med de 2 inputtene som argument
    spill1 = Spillebrett(inp2, inp1)

    #tom input, for å ikke spørre brukeren om noe før while-løkken har kjørt
    inp = ""
    #mens inp ^ (og inne i løkken) ikke er Q, kjøres koden
    while inp != "q":
        #stor linjeskift
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        #lager en border rundt rutenettet på lengden til radene
        border = ""
        for x in range(inp1):
            border += "---"
        print(border)

        #kaller opp objektet med 2 metoder som tegner rutenettet, og deretter oppdateren den
        spill1.tegnBrett()
        spill1.oppdatering()

        #Antall levende celler blir printet ut vha metoden "finnAntallLevende()"
        print("Antall levende celler: ", spill1.finnAntallLevende())
        print(border)

        #input som spør brukeren om de vil avslutte eller fortsette - henger sammen med while-løkken
        inp = input("Press enter for å fortsette. Skriv in q og trykk enter for å avslutte: ")
    print(""), print("")

# starter hovedprogrammet
main()