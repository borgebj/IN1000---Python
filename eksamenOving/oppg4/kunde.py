
class Kunde:

    def __init__(self, nr, unngaListe):
        self._nr = nr
        self._liste = unngaListe

    def velgRetter(self, meny):
        redMeny = meny.hentRedusertMeny(self._liste)
        beskjed = []
        rettNavn = []

        for x in redMeny:
            print("\n - ",x," - ")
            rettListe = redMeny[x].hentOkRetter(self._liste)

            for x in rettListe:
                print(x)
                rettNavn.append(x.hentNavn())

            inp = input("Hvilken rett onsker du?: ")
            if inp != "":
                while inp not in rettNavn:
                    print("\nDen retten finnes ikke")
                    inp = input("Hvilken rett onsker du?: ")
                    print("\n")
                beskjed.append(str(inp))

            print("-----------------------------------------")
        return beskjed