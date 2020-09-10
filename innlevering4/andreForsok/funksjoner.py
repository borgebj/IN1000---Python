print("---------------------------------\n")

# adderer param1 med param2 og returnerer
def adder(tall1, tall2):
    return (tall1+tall2)

# 2 eksempler paa adder-funksjon
print("5 + 9 =", adder(5, 9))
print("-6 + -4 =", adder(-6, -4))


# funksjon som teller hvor mange ganger param2 forekommer i teksten param1
def tellForekomst(minTekst, minBokstav):
    count = 0
    for hver in tekst:
        if (hver == bokstav):
            count += 1
    return count

# spoer bruker om tekst og boksatv
tekst = input("\nSkriv inn en setning/ord\n> ")
bokstav = input("\nSkriv en bokstav\n> ")

# lagrer antall i en variabel og forteller bruker
count = tellForekomst(tekst, bokstav)
print("Bokstaven ["+bokstav+"] forekommer", count, "antall ganger i setninge/ordet ["+tekst+"]")


print("\n---------------------------------")
