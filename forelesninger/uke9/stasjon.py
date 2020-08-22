print("-----------------------------------------")

#Lenkede lister eksempel

class Stasjon:

    def __init__(self, navn):
        self._navn = navn
        self._nabo = None

    def sett_nabo(self, nabo):
        self._nabo = nabo

    def hent_navn(self):
        return self._navn

    def hent_nabo(self):
        return self._nabo

def hovedprogram():
    trikkestall = Stasjon("stallen")
    forrige = trikkestall

    for stasjonsnavn in open("trase.txt"):
        denne = Stasjon(stasjonsnavn.strip())
        forrige.sett_nabo(denne)
        forrige = denne

    maal = input("Hvor vil du reise til? ")
    lokasjon = trikkestall
    while lokasjon.hent_navn() != maal.lower():
        lokasjon = lokasjon.hent_nabo()
        print(lokasjon.hent_navn())

hovedprogram()


print("------------------------------------------")