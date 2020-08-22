# coding=utf-8
import random
import time

#bingo-tabellen. 3 rader
minBingo1 = []
minBingo2 = []
minBingo3 = []

#tom liste som består av tall som er i tabellen
brukt = []

#prosedyrer som sjekker om tall allerede er i bingotabell
def rad1():
    rad1 = random.randint(10,60)

    if rad1 in brukt:
        rad1 = random.randint(10,60)
        minBingo1.append(rad1)
        brukt.append(rad1)
    else:
        minBingo1.append(rad1)
        brukt.append(rad1)
def rad2():
    rad2 = random.randint(10,60)

    if rad2 in brukt:
        rad2 = random.randint(10,60)
        minBingo2.append(rad2)
        brukt.append(rad2)
    else:
        minBingo2.append(rad2)
        brukt.append(rad2)
def rad3():
    rad3 = random.randint(10,60)

    if rad3 in brukt:
        rad3 =  random.randint(10,60)
        minBingo3.append(rad3)
        brukt.append(rad3)
    else:
        minBingo3.append(rad3)
        brukt.append(rad3)

#rad 1 i tabell
rad1()
rad1()
rad1()
#rad 2 i tabell
rad2()
rad2()
rad2()
#rad 3 i tabell
rad3()
rad3()
rad3()

#printer ut bingolisten til brukeren. består av 3 lister som utgjør en 3x3 tabell
print("Min bingoliste")
print(minBingo1)
print(minBingo2)
print(minBingo3)

minRiktig = []

time.sleep(3)

print("\nFor å vinne 'bingo' må du få 3 riktige tall\n")
print("Du kommer til å få 5 forsøk. Det vil altså komme 5 tilfeldige tall\n")

time.sleep(2)

minTotal = minBingo1 + minBingo2 + minBingo3

#her starter "bingo-kastet"
def bingoKast():

    tall = random.randint(10, 60)

    print("Tallet ble:",tall)

    time.sleep(1)

    if tall in minTotal:
        minRiktig.append(tall)
        print("Gratulerer! Du har", len(minRiktig), "riktige tall")
        time.sleep(1)
        print("Mine riktige tall:",minRiktig,"\n")
    else:
        print("Feil. Du har",len(minRiktig),"riktige tall")
        time.sleep(1)
        print("Mine riktige tall:",minRiktig,"\n")

    time.sleep(1)

def slutt():
    if len(minRiktig) == 3:
        print("\nGratulerer! Du vant dette 'bingo' spillet")
    else:
        print("\nDu vant ikke.","Du endte opp med", str(len(minRiktig))+"/3","riktige tall.")

def vunnet():
    if len(minRiktig) == 3:
        slutt()

#mange prosedyrer går i gang
bingoKast()
time.sleep(1)
bingoKast()
time.sleep(1)
bingoKast()
vunnet()
time.sleep(1)
bingoKast()
vunnet()
time.sleep(1)
bingoKast()
vunnet()
slutt()
