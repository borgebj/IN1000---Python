import random
import sys

class Hangman:
    def __init__(self, valg):
        self._tempSetning = []
        self._feilOrd = []
        self._antForsok = 8
        self._gjettet = False
        self._fullSetning = self.hentListe(valg.lower())

        if (len(self._fullSetning)<=0):
            print(valg, "er ikke et valg")
            sys.exit()

        self.opprettTemp()
        self.displayTemp()

    def hentListe(self, vanskelighet):
        if (vanskelighet.lower() == "enkelt"): return random.choice(["kake", "kjeks", "tomat", "potet", "bil", "hund", "katt", "tekopp", "brus", "godteri", "bruh moment"])
        elif (vanskelighet.lower() == "vanskelig"): return random.choice(["vaskemaskin", "matbutikk", "sommerferie", "datamaskin", "oppvaskmiddel", "Aquarium", "Racingrally", "mobiltelefon"])
        else: return []


    def opprettTemp(self):
        for ord in self._fullSetning:
            self._tempSetning.append("_ ")

    def displayMan(self):
        print()
        if (self._antForsok < 1):
            print("-------  ")
        if (self._antForsok < 2):
            print("|     |  ")
        if (self._antForsok < 4):
            print("|     O  ")
        if (self._antForsok < 6):
            print("|    /--\ ")
        if (self._antForsok < 8):
            print("|     /\  ")
        print()


    def displayTemp(self):
        print("\n\nDu har", self._antForsok, "antall forsok")
        print(self._feilOrd,"\n")
        self.displayMan()
        for ord in self._tempSetning:
            print(ord, end="")

    def duplicates(self, lst, item):
        return [i for i, x in enumerate(lst) if x == item]

    def gjettOrd(self, bokstav):
        if bokstav in self._fullSetning:
            revealIndekser = self.duplicates(self._fullSetning, bokstav)
            for indeks in revealIndekser:
                self._tempSetning[indeks] = bokstav+" "
        else:
            self._feilOrd.append(bokstav)
            self._antForsok -= 1
            print("\n\n", bokstav, "er feil")
        if "_ " not in self._tempSetning:
            self._gjettet = True
        self.displayTemp()

    def hentGjettet(self):
        return self._gjettet

    def hentForsok(self):
        return self._antForsok

    def hentOrd(self):
        return self._fullSetning

def hovedprogram():
    valg = input("\n\nHvilken vanekslighetsgrad? (enkelt/vanskelig): ")
    hangman = Hangman(valg)

    while hangman.hentGjettet() == False and hangman.hentForsok() > 0:
        bokstav = input("\nGjett en bokstav: ")
        hangman.gjettOrd(bokstav)

    if hangman.hentForsok() <= 0:
        print("\n\nIngen flere forsok, du tapte")
        print("Ordet var:", hangman.hentOrd(), "\n")
    elif hangman.hentGjettet():
        print("\nDu vant!\n")

hovedprogram()
