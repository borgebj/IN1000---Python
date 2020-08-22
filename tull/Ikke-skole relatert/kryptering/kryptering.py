import getpass

# Program som krypterer ditt passord (enkel versjon)

alfabet = {"a":"d", "b":"e", "c":"f", "d":"g", "e":"h", "f":"i", "g":"j", "h":"k", "i":"l", "j":"m", "k":"n", "l":"o", "m":"p", "n":"q", "o":"r", "p":"s", "q":"t", "r":"u", "s":"v", "t":"w", "u":"x", "v":"y", "w":"z", "x":"a", "y":"b", "z":"c",
           "!":"¤", '"':"%", "#":"&", "¤":"/", "%":"(", "&":")", "/":"=", "(":"?", ")":"!", "=":'"', "?":"#",
           "1":"3", "2":"4", "3":"5", "4":"6", "5":"7", "6":"8", "7":"9"," 8":"1", "9":"2", "0":"3"}


def hovedprogram():
    print("---------------------------------------------\n")

    inp = getpass.getpass("Hva er ditt passord: ")
    liste = list(inp.lower())


    kryptert = []

    print("\n" f'{"Før kryptering:":20}'+" ( ", inp, " ) ")

    for x in liste:
        if x in alfabet:
            kryptert.append(alfabet[x])

    nytt = "".join(kryptert)
    print(f'{"Etter kryptering:":20}'+" ( ", nytt, " ) ")

    print("\n---------------------------------------------")


hovedprogram()

