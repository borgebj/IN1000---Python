
class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag = nyDag
        self._maaned = nyMaaned
        self._aar = nyttAar

    def lesAar(self):
        return "Aaret er "+str(self._aar)

    def __str__(self):
        return (str(self._dag)+"."+str(self._maaned)+"."+str(self._aar))

    # tar inn kun en dag, og sjekker om dato er denne
    def sjekkDag(self, dag):
        if self._dag == dag:
            return True
        else: return False