print("---------------------------------\n")

steder = []
for x in range(5):
    steder.append(input("Hvor onsker du aa reise?\n> "))

klesplagg = []
avreisedatoer = []
for x in range(5):
    klesplagg.append(input("Klessplagg du onsker aa ta med?\n> "))
    avreisedatoer.append(input("Avreisedato du onsker aa dra?\n> "))

reiseplan = [steder, klesplagg, avreisedatoer]
print("\nDin reiseplan:")
i = 0
for liste in reiseplan:
    print(i, "-", liste)
    i += 1

# spoer bruker hvilken liste og hvilket element
i1 = int(input("\nListe-indeks: "))
i2 = int(input("Element-indeks: "))

# sjekker om tallene er innenfor rekkevidde og dermed printer ut
if (0 <= i1 <= len(reiseplan)-1 and 0 <= i2 <= len(reiseplan[i1])-1):
    print("\nDu valgte:", reiseplan[i1][i2] )
else:
    print("Ugyldig input!")


print("\n---------------------------------")
