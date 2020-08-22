from hund import Hund

#bruk-ish i oblig 8???

class Kennel:

    def __init__(self, rad, kol):
        self._rad = rad
        self._kolonner = kol
        self._hundeliste = self.generer(rad, kol)

    def generer(sel, rader, kolonner):
        navneliste = ["Ace", "Aiden", "Allegro", "Andres", "Avalon", "Ashes", "Aspen", "Amigo", "Amazon", "Armani", "August", "Anaconda", "Android"]
        maksAlder = 15
        hundeliste = []
        for x in range(rader):
            hundeliste.append([])
            for y in range(kolonner):
                kjonn = randint(0, 1)
                navnIndeks = randint(0, len(navneliste)-1)
                alder = randint(0, maksAlder)
                hundeliste[x].append(hund(kjonn, navneliste[navnIndeks], alder))
        return hundeliste

    def hentHund(self, rad, kol):
        return self._hundeliste[rad][kol]