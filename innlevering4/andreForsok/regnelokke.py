print("---------------------------------\n")

# tom liste som inneholder tallene brukt
tallListe = []

# spoer om tall helt til bruker taster 0
tall = int(input("Skriv et tall: "))
while tall != 0:
    tallListe.append(tall)
    tall = int(input("Skriv et tall: "))


# printer ut alle tallene i listen
print("\nDine tall:")
for tall in tallListe:
    print("["+str(tall)+"]", end=" ")


# summerer alle tallene i listen
minSum = 0
for tall in tallListe:
    minSum += tall
print("\n\nDin sum:", minSum)


# finner det minste tallet
minste = tallListe[0]
for tall in tallListe:
    if tall < minste:
        minste = tall
print("\nMinste element:", minste)


# finner det storste tallet
storste = tallListe[0]
for tall in tallListe:
    if tall > storste:
        storste = tall
print("\nStorste element:", storste)
print("\n---------------------------------")
