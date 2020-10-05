print("---------------------------------\n")


def lagBrukernavn(navn, studentBok):
    navnListe = navn.split()
    brukernavn = navnListe[0]+navnListe[1][0]
    tall = 1

    # 4.7 tar hensyn til duplikater - extender navn hvis finnes
    while brukernavn in studentBok:
        ekstradel = navnListe[1][tall]
        brukernavn += ekstradel
        ekstradel += ekstradel
        tall += 1
    return brukernavn


def lagEpost(brukernavn, suffix):
    return (brukernavn+"@"+suffix)


def printEposter(ordbok):
    for element in ordbok:
        print( lagEpost(element, ordbok[element]) )


def registrer(studentBok):
    navn = input("\nSkriv inn navn: ")
    suffix = input("Skriv inn suffix: ")
    brukernavn = lagBrukernavn(navn, studentBok)
    studentBok[brukernavn] = suffix

def registrerTest(studentBok):
    navn = "borge bjornstadjordet"
    suffix = "uio.no"
    brukernavn = lagBrukernavn(navn, studentBok)
    print(brukernavn)
    assert brukernavn == "borgeb"
    studentBok[brukernavn] = suffix


def printBok(studentBok):
    print()
    printEposter(studentBok)
    print()


def hovedprogram():
    studentBok = {}
    inp = ""
    while inp.lower() != "s":
        print("i : registrer navn og suffi")
        print("p : print ut ordbok")
        print("s : avslutt")
        inpTo = input("Valg > ")

        if inpTo.lower() == "i":
            #registrer(studentBok)
            registrerTest(studentBok)

        elif inpTo.lower() == "p":
            printBok(studentBok)


hovedprogram()


print("\n---------------------------------")