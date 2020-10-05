
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()


# "minFunksjon"- defineres foerst som ikke tar noen parametere
# deretter defineres hovedprogram uten paraemtere heller.
# inne i hovedprogram defineres foerst to variabler (a og b),
# deretter printes ut variabelen b. b blir saa endret til a
# (b variabel faar verdien til a) a endrer saa sin verdi til et kall
# paa funksjonen "minFunksjon"
# inne i "minFunksjoN" starter en lokke som gaar 2 ganger:
# inne i lokken blir variabel c definert og saa printet ut.
# c blir saa inkremert med 1, og en ny variabel blir definert (b)
# b blir saa inkremert med a som ikke er definert, og saa printes ut b
# etter lokken har kjort to ganger (printet c 2 ganger, inkremert c 2 ganger
# og printet ut b 2 ganger) returneres verdien b
# paa slutten av hovedprogram() printes baade a og b

# her kommer det etterhvert feilmelding pga a inne i "minFunksjon" ikke er definert