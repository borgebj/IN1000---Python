# coding=utf-8
import random
import time

print("--------BINGO--------")

brukt = []

for i in range(5):
    rad = []
    for e in range(5):
        tall = random.randint(10,60)

        while tall in brukt:
            tall = random.randint(10,60)

        brukt.append(tall)
        rad.append(tall)
        time.sleep(0.04)
    print(rad)

print("---------------------")

time.sleep(2)
x = 1
mineTall = []
print("\nBingo vil nå starte og terningen vil bli kastet")
print("Du får 5 forsøk på å vinne, du trenger 3 eller høyere.")
time.sleep(3)
while x <= 5:
    kast = random.randint(10,60)
    print("\nKast nr", x, "ble", kast)
    x += 1
    time.sleep(1)
    if kast in brukt:
        print("Du har dette tallet!")
        mineTall.append(kast)
    else:
        print("Du har ikke dette tallet.")
    time.sleep(2)

if len(mineTall) >= 3:
    print("\nDu har vunnet bingospillet mitt! Gratulerer. 10 kroner vil bli satt inn på kontoen din")
else:
    print("\nDu har tapt bingospillet. 200kr vil bli trukket fra kontoen din.\n")
