from takeaway import TakeAway

def hovedprogram():
    print("-------------------------------------------------------------\n")
    takeaway = TakeAway(["frokost", "middag", "kveldsmat"], "kunder.txt")

    print("   -   TakeAway-program for kunder   -   \n")

    inp = input("Telefonnummer?: ")
    while len(inp) != 8 and type(inp) != int:
        print("\nDu skrev feil, skriv inn på nytt.")
        inp = input("Telefonnummer?: ")

    while inp != "":
        takeaway.betjenKunde(inp)
        inp = input("\nTelefonnummer?: ")
    print("\n-------------------------------------------------------------")

hovedprogram()