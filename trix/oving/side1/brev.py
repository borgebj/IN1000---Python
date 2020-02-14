
class Brev:

    def __init__(self, avsender, mottaker):
        self._avsender = avsender
        self._mottaker = mottaker
        self._liste = []

    def skrivLinje(self, tekst):
        self._liste.append(tekst)

    def lesBrev(self):
        print("\nHei,",self._mottaker+"!\n")
        for x in self._liste:
            print(x)
        print("\nHilsen fra",self._avsender,"\n")


def hovedprogram():

    brev = Brev("Borge Bjornstadjordet", "Mikkel Arnesund")
    brev.skrivLinje("Hvordan har du det?")
    brev.skrivLinje("Jeg har det godt jeg")
    brev.lesBrev()

hovedprogram()