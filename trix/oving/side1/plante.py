
class Plante:

    def __init__(self, maksgrenseVann):
        self._vannbeholder = 0
        self._maks = maksgrenseVann
        self._levende = True

    def vannPlante(self, vannCl):
        self._vannbeholder += vannCl
        if self._vannbeholder > self._maks:
            self._levende = False

    def nyDag(self):
        self._vannbeholder -= 20
        if self._vannbeholder < 0:
            self._levende = False

    def levende(self):
        if self._levende:
            return self._levende
        else:
            return self._levende

def hovedprogram():

    plante1 = Plante(40)
    plante2 = Plante(90)

    plante1.vannPlante(10)
    plante2.vannPlante(10)

    plante1.nyDag()
    plante1.nyDag()
    plante2.nyDag()
    plante2.nyDag()

    print("")
    print("Er plante 1 levende?:", plante1.levende())
    print("Er plante 2 levende?:", plante2.levende())
    print("")

hovedprogram()