# coding=utf-8
"""Dette programmet tar vare på ulike lister, samtidig som programmet henter inn verdier fra brukeren gjennom input-felt, og legger disse inn i listene. Programmet legger til og multipliserer også tall og lister, og skriver disse ut til terminalen"""
#En variabel som inneholder en liste med 3 verdier blir opprettet.
liste1 = [3, 6, 9,]

#legger til et tall i listen, altså tallet 12. Kan også skrives: "liste[3] = 12"
liste1.append(12)

#Det første tallet (0) og det siste tallet (3) blir printet ut.
print(liste1[0], "og", liste1[2],"\n")

#Definere variabel for ny liste
listeny = []

#En prosedyre som legger til ny verdi til listen gjennom input fra brukeren.
#Append gjør at det som blir skrevet inn i input blir lagt til i listen "liesteny"
def navn():
    listeny.append(input("Skriv inn navn: ").lower())

#prosedyren blir kalt opp 4 ganger
navn()
navn()
navn()
navn()

#Hvis navnet mitt er i menyen, vil programmet printe ut "Du husket meg!", ellers "Glemte du meg?". Navnet mitt kommer i listen om brukeren skriver inn navnet i de 4 input-feltene.
if "børge".lower() in listeny:
    print("\nDu husket meg!\n")

else:
    print("\nGlemte du meg?\n")

#multipliserer sammen de 3 verdiene i liste1
produkt = liste1[0] * liste1[1] * liste1[2] * liste1[3]

#legger sammen de 3 verdiene i liste1
sum = liste1[0] + liste1[1] + liste1[2] + liste1[3]

#Variabel som holder en tom liste
liste2 = []

#variabelene produkt og sum blir lagd til med append til den tomme listen.
liste2.append(produkt)
liste2.append(sum)

#De to listene blir lagt sammen til en ny variabel kalt storListe.
storListe = liste1 + liste2

#printer ut den nye listen til terminalen.
print(storListe)

#pop vil si at en verdi blir fjernet. Pop uten verdi vil fjerne det siste elementet i listen. Gjør vi dette to ganger, fjernes de 2 siste. (kan også skrives storListe.pop(-1) og storListe.pop(-2)
storListe.pop(5)
storListe.pop(4)

#printer ut den nye listen uten de to siste verdiene.
print(storListe)

