"""Dette programmet henter inn tall fra en tekst-fil, putter disse inn i en tom liste, og deretter regner ut gjenomsnitten av temperaturen"""

print("------------------------------------------------------------\n")

#variabel for tom liste.
liste = []

#variabelen "minFil" blir definert som innholdet til "temperatur.txt"
minFil = open("temperatur.txt")

#for-løkke som legger til hvert element i "minFil" til den tomme listen.
for x in minFil:
    liste.append(x)

#funksjon som regner gjennomsnittet av listen "x"
def gjenomsnitt(x):
    sum = 0
    #for-løkke som legger sammen hvert element og legger det i en variabel.
    for a in x:
        sum += int(a)
    #printer ut tekst sammen med gjennomsnittet, regnet gjennom summen / lengden til listen(antall tall)
    print("Gjennomsnittet av de ulike temperaturene er: ", sum/len(liste))

#kaller opp funksjonen med listen som argument.
gjenomsnitt(liste)

print("\n-----------------------------------------------------------")