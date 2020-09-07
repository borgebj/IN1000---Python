
# tom liste med 3 tall
liste =  [-3, 6, 10]

#legger til tallet 2 i listen
liste.append(-2)

#skriver ut forste og tredje element
print(f'Forste tall: {liste[0]}, Tredje tall: {liste[2]}')

tomListe = []

# ber bruker legge inn et navn i den tomme listen 4x ganger - saa legger den til
for x in range(4):
    tomListe.append(input("Skriv et navn\n> "))

# sjekker om navnet mitt er i listen
if ("borge" in tomListe):
    print("Du husket meg!")
else:
    print("Glemte du meg?")


nyListe = []

sum = 0
produkt = 1

# legger legger sammen alle tall i listen og lagrer i variabel, gjoer det samme for mulitplikasjon i en annen variabel
for tall in liste:
    sum += tall
    produkt *= tall

# legger til produkt og sum til nye listen
nyListe.append(sum)
nyListe.append(produkt)

# legger sammen den gamle og den nye listen
sammenslattListe = liste + nyListe

# printer ut sammenslatt
print(sammenslattListe)

# fjerner de 2 siste vha pop
sammenslattListe.pop()
sammenslattListe.pop()

# printer ut sammenslatt
print(sammenslattListe)
