from sykdom import Sykdom
from sykdomskatalog import SykdomdsKatalog

katalog = SykdomdsKatalog("sykdommer_test.csv")

"""sykdom = Sykdom("Kolera")
sykdom.legg_til_posisjon(10)
sykdom.legg_til_posisjon(20)

assert sykdom.er_assosiert(10) == True
assert sykdom.er_assosiert(20) == True
assert sykdom.er_assosiert(15) == False"""