# coding=utf-8
"""Dette programmet bruker while-løkker og for-løkker til flere ting som for eksempel å sjekke gjentatte ganger input fra brukeren og dermed legge disse i og printe ut en liste, og for løkker som sjekker listen og skriver det største og minste tallet"""

#for å få bedre oversikt i terminalen.
print("---------------------------------------------------------\n")

#tom liste
liste = []

#tall blir definert av brukeren.
tall = int(input("Skriv inn et tall: "))
liste.append(tall)


#om tall IKKE er lik 0, blir brukeren fortalt å prøve igjen og løkken fortsetter.
while tall != 0:
    tall = int(input("Prøv igjen: "))
    #samtidig som å fortelle brukeren å prøve igjen, legger den til tallet i den tomme listen.
    liste.append(tall)
print("\nElementer i listen")
#for løkke som printer hvert element i listen.
for loekke in liste:
    print("-", loekke)

#variabel med verdi 0
minSum = 0

#for-løkke som legger til variabel "x" til den tomme variabelen "minSum" for hvert tall i listen.
for x in liste:
    minSum += x

#printer ut summen av listen.
print("\nSummen av dine forsøk:", minSum,"\n")

minste = liste[0]
#for-løkke som finner og printer ut det minste tallet.
for a in liste:
    # om tallet i listen er mindre enn første indeks i liste, blir variabelen minste nå tallet i listen.
    if a < minste and a != 0:
        minste = a

print("Det minste tallet:", minste)

#Variabelen stor definert som første indeks i liste
stor = liste[0]
#for-løkke som finner og printer ut det største tallet.
for b in liste:
    # om tallet i listen er større enn første indeks i liste, blir variabelen stor nå tallet i listen.
    if b > stor:
        stor = b

print("Det største tallet:", stor)

print("\n-------------------------------------------------------")














