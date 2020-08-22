print("-------------------------------------------------------")

#rektangel
class Rektangel:
    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    def areal(self):
        return self._lengde*self._bredde

    def endre(self, lengde, bredde):
        self._lengde += lengde
        self._bredde += bredde

def hovedprogram():
    rektangel = Rektangel(5, 6)
    sirkel = rektangel
    print("Er sirkel = rektangel?? -", sirkel is rektangel)

    print("Nytt areal:", sirkel.areal())

    rektangel.endre(2, 3)
    print("Nytt areal:", sirkel.areal())
hovedprogram()

print("-------------------------------------------------------")
