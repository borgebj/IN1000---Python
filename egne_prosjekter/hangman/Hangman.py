from random import randint
import sys

class Hangman:
    def __init__(self, valg):
        self._fullSetning = []
        self._tempSetning = []
        self._antForsok = 6
        self._gjettet = False
        liste = self.hentListe(valg.lower())

        if (len(liste)<=0):
            print(valg, "er ikke et valg")
            sys.exit()
        else:
            self._fullSetning = liste[randint(1, len(liste)-1)]

        self.opprettTemp()
        self.displayTemp()

    def hentListe(self, vanskelighet):
        if (vanskelighet.lower() == "enkelt"): return ["kake", "kjeks", "tomat", "potet", "bil", "hund", "katt", "tekopp", "brus", "godteri"]
        elif (vanskelighet.lower() == "vanskelig"): return ["vaskemaskin", "matbutikk", "sommerferie", "datamaskin", "oppvaskmiddel", "Aquarium", "Racingrally", "mobiltelefon"]
        else: return []


    def opprettTemp(self):
        for ord in self._fullSetning:
            self._tempSetning.append("_ ")

    def displayMan(self):
        print()
        if (self._antForsok < 1):
            print("-------  ")
        if (self._antForsok < 3):
            print("|     |  ")
        if (self._antForsok < 4):
            print("|     O  ")
        if (self._antForsok < 5):
            print("|    /--\ ")
        if (self._antForsok < 6):
            print("|     /\  ")
        print()

    def displayTemp(self):
        print("\n\nDu har", self._antForsok, "antall forsok\n")
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